#driver function spell_check takes the word as an argument and returns a list of suggesions
#Author Akshatha dtd 11/3/15

from Levenshtein import *
import operator
import dawg
import word_roman_mod
from word_roman_mod import * 
dictWords=[]
fr={}
keys=[]
suggests=[]


#for predixtons to sweep the whole word
global spell_done
global done
global final_suggests
spell_done=0
done=0
final_suggests=[]
#holder for reverse dictionary
rev_dictWords=[]

to_merge_file = open("dictionary_15k.txt", "r")
for line1 in to_merge_file:
	dictWords.append(line1.strip())

#read the store the reverse dictionary
rev_f=open("reverse_dictionary_15k.txt","r")
for line in rev_f:
	rev_dictWords.append(line.strip())
				
#creating the reverse dawg
rev_dict_dawg=dawg.CompletionDAWG(rev_dictWords)
dict_dawg=dawg.CompletionDAWG(dictWords)

recent=[]
recent.append("")
recent.append("")
recent.append("")
recent.append("")
recent.append("")

def set_done():
	global spell_done
	#print("setting done")
	spell_done=1
#defining driver for spell checker
def spell_check(to_check, direction, begin_letter):
	suggests=[]
	
	to_merge_file = open("dictionary_15k.txt", "r")
	for line1 in to_merge_file:
		dictWords.append(line1.strip())

#read the store the reverse dictionary
	rev_f=open("reverse_dictionary_15k.txt","r")
	for line in rev_f:
		rev_dictWords.append(line.strip())
				
#creating the reverse dawg
	rev_dict_dawg=dawg.CompletionDAWG(rev_dictWords)
	dict_dawg=dawg.CompletionDAWG(dictWords)

	#the suggestions that are to be returned ; ordered and shit
	
	if direction=='r':
		dictionary=rev_dictWords
		used_dawg=rev_dict_dawg
	else:
		dictionary=dictWords
		used_dawg=dict_dawg
	
	#only requiredwords from dict
	required_words=used_dawg.keys(begin_letter)
	
	for word in required_words:
		d=distance(to_check,word)
		if d==1:
			suggests.append(word)
			
	#adding morphology		
	morphWords=[]		
	morph_suggests=[]
	file_morph=open("morph_forms.txt","r")
	for line in file_morph:
		morphWords.append(line.strip())
	for word in morphWords:
		d=distance(to_check,word)
		if d==1:
			suggests.append(word)
	
	return suggests
	
def order_suggests(suggests):
	intersection1=set(suggests).intersection(keys)
	intersection=list(intersection1)
	done=[]
	ret_suggests=[]
	bigk=""
	bigv=0
	for i in range(0,len(intersection)):
		bigk=""
		bigv=-1
		for j in range(0,len(intersection)):
			if fr[intersection[i]] > bigv:
				bigk=intersection[i]
				bigv=fr[intersection[i]]
		done.append(intersection[i])
	
	for word in done:
		if word in recent:
			ret_suggests.append(word)
			
	for word in done:
		if word not in recent:
			ret_suggests.append(word)
	
	for word in suggests:
		if word not in done:
			ret_suggests.append(word)
			
	return ret_suggests		
	
#orders and keeps the suggestions adding if the spelling is not yet traversed atleast once	
def select_suggest(given_suggests,prnt_res):
	global final_suggests
	global spell_done
	global done
	#if spell_done==0:
	#final_suggests=final_suggests+given_suggests
	final_suggests=given_suggests
	#else:
	to_return_to_sandhimod = print_suggestions(prnt_res)
	return to_return_to_sandhimod
	
def print_suggestions(prnt_res):
#print things in kannada
	print("here is prnt_res",prnt_res)
	global final_suggests
	if prnt_res==3:
		kan_suggests=[]
		
		
		if not final_suggests:
			return 'notthere'
			
		print("\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ")
		suggests=order_suggests(final_suggests)
		print(suggests)
		for word in suggests:
			print(word)
			print(to_uni(word))
			kan_suggests.append(to_uni(word))
		print("printing what is returned")
		for word in kan_suggests:
			print(word)
		return kan_suggests
		
		
#print in eng
	else:
		#global final_suggests
		if not final_suggests:
			return 'notthere'
			
		print("\nDid you mean?")
		suggests=order_suggests(final_suggests)
		
		print(suggests)
		print("done")
		return suggests
		
		
		
def pick_selected(selected,prnt_res):
	global final_suggests
	if prnt_res==3:
		k=-1
		k=k+1
		p=k%5
	
		recent[p]=selected
		
		if selected not in keys:
			keys.append(selected)
			fr[selected]=0
		else:
			fr[selected]=fr[selected]+1
		final_suggests=[]
		return selected
	else:
		k=-1
		print("\nYou have selected : ",selected)
		
		k=k+1
		p=k%5
	
		recent[p]=selected
		
		if selected not in keys:
			keys.append(selected)
			fr[selected]=0
		else:
			fr[selected]=fr[selected]+1
		final_suggests=[]
		print("fr is")
		print(fr)
		return selected
	
