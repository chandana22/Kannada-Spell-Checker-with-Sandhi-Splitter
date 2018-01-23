import correct_sandhi_mod
from correct_sandhi_mod import *
import word_roman_mod
from word_roman_mod import *
import add_word_mod
from add_word_mod import *
import pratyaya_chopper_driver_mod
from pratyaya_chopper_driver_mod import *
import os
import prefix_suffix_mod
from prefix_suffix_mod import *
from Levenshtein import *
ans='y'

#everything in kannada as the user knows kannada

def spell_check_kan(uni_word):
	correct_selected=[]
	morphWords=[]
	sug=''
	#to return multiple values
	#first value has the correct value 1 or 0 depending on if it is correct or not
	#the second value has what to print if it is correct
	#third has a list of suggestions
	
	#removing pratyaya if it has any
	#check_word=pratyaya(check_word)
	check_word=to_roman(uni_word)
	print("after removing pratyaya",check_word)
	
	correct_selected.append(0)
	correct_selected.append("")
	correct_selected.append("")
	correct_selected.append("")
	correct=0
	found=0
	selected=''
	f = open("dictionary_15k.txt", "r")
	for line1 in f:
		dictWords.append(line1.strip())
	dict_dawg=dawg.CompletionDAWG(dictWords)
	f.close()
	
	#adding morphology words
	file_morph=open("morph_forms.txt","r")
	for line in file_morph:
		morphWords.append(line.strip())
	morph_dawg=dawg.CompletionDAWG(morphWords)
	file_morph.close()	
		
	if check_word in dict_dawg:
		correct=1
	elif check_word in morph_dawg:
		correct=1
				
	found_print=sandhi_splitter(check_word,4)
	if found_print[0]==1:
		correct_selected[1]="ಈ ಪದವು ಸಂಧಿ ಪದವಾಗಿದೆ!\n"+found_print[1]
		print("ಈ ಪದವು ಸಂಧಿ ಪದವಾಗಿದೆ")
		correct=1
	
	if correct==1:
		correct_selected[1]+="\nಈ ಪದವು ಸರಿಯಾದ ಪದವಾಗಿದೆ!"
		print("ಈ ಪದವು ಸರಿಯಾದ ಪದವಾಗಿದೆ!")
	else:
		suggests=spell_check(check_word,'f','')
		ret_suggests=order_suggests(suggests)
		if len(ret_suggests)>0:
			select_suggest(ret_suggests,3)
			selected=print_suggestions(3)
		else:
			selected=spell_sandhi_checker(check_word,3)
			prefix_suffix_found_print=prefix_suffix(check_word,3)
			print("prefix suffix over")
			if prefix_suffix_found_print[0]==1:
				if selected=='notthere' or selected=='':
					sug=prefix_suffix_found_print[1]
					print("printing sug")
					print(sug)
				else:
					sug=selected+prefix_suffix_found_print[1]
					print("printing pre")
					print(prefix_suffix_found_print[1])
			print("printing sug")
			print(sug)
			if len(sug)!=0:
				ordered_suggests=order_suggests(sug)
				selected=select_suggest(ordered_suggests,0)
			
					#need to change these sentences. and to make prnt_res =4 in check_mod sariya didnt give suggestions. check once
	correct_selected[0]=correct
	correct_selected[2]=selected
	#if prefix_suffix_found_print[2]!='':
	#	correct_selected[3]=prefix_suffix_found_print[2]
	return correct_selected
	
	
	
	
	
	
	

		
	if correct==1:
		correct_selected[1]+="\nಈ ಪದವು ಸರಿಯಾದ ಪದವಾಗಿದೆ!"
		print("ಈ ಪದವು ಸರಿಯಾದ ಪದವಾಗಿದೆ!")
	else:
		suggests=spell_check(check_word,'f','')
		ret_suggests=order_suggests(suggests)
		if len(ret_suggests)>1:
			select_suggest(ret_suggests,3)
			selected=print_suggestions(3)
		else:
			selected=spell_sandhi_checker(check_word,3)
	#need to change these sentences. and to make prnt_res =4 in check_mod sariya didnt give suggestions. check once
	correct_selected[0]=correct
	correct_selected[2]=selected
	return correct_selected
		
def spell_check_eng(check_word):
	correct_selected=[]
	sug=''
	morphWords=[]
	#to return multiple values
	#first value has the correct value 1 or 0 depending on if it is correct or not
	#the second value has what to print if it is correct
	#third has a list of suggestions
	
	#removing pratyaya if it has any
	#check_word=pratyaya(check_word)
	print("after removing pratyaya",check_word)
	
	correct_selected.append(0)
	correct_selected.append("")
	correct_selected.append("")
	correct_selected.append("")
	correct=0
	found=0
	selected=''
	f = open("dictionary_15k.txt", "r")
	for line1 in f:
		dictWords.append(line1.strip())
	dict_dawg=dawg.CompletionDAWG(dictWords)
	f.close()
	
	#adding morphology words
	file_morph=open("morph_forms.txt","r")
	for line in file_morph:
		morphWords.append(line.strip())
	morph_dawg=dawg.CompletionDAWG(morphWords)
	file_morph.close()	
		
	if check_word in dict_dawg:
		correct=1
	elif check_word in morph_dawg:
		correct=1		
	found_print=sandhi_splitter(check_word,2)
	if found_print[0]==1:
		correct_selected[1]="The given word is a sandhi word!\n"+found_print[1]
		print("The given word is a sandhi word")
		correct=1
	if correct==1:
		correct_selected[1]+="\n\nThe word is correct!!"
		print("\nThe word is correct!!")
	else:
		suggests=spell_check(check_word,'f','')
		ret_suggests=order_suggests(suggests)
		if len(ret_suggests)>0:
			select_suggest(ret_suggests,1)
			selected=print_suggestions(1)
		else:
			selected=spell_sandhi_checker(check_word,1)
			prefix_suffix_found_print=prefix_suffix(check_word,0)
			print("prefix suffix over")
			if prefix_suffix_found_print[0]==1:
				if selected=='notthere' or selected=='':
					sug=prefix_suffix_found_print[1]
				else:
					sug=selected+prefix_suffix_found_print[1]
			if len(sug)!=0:
				ordered_suggests=order_suggests(sug)
				selected=select_suggest(ordered_suggests,0)
			
					#need to change these sentences. and to make prnt_res =4 in check_mod sariya didnt give suggestions. check once
	correct_selected[0]=correct
	correct_selected[2]=selected
	#if prefix_suffix_found_print[2]!='':
	#	correct_selected[3]=prefix_suffix_found_print[2]
	return correct_selected
