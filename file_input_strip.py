#mode are like 1 for spell checker, 2 for sandhi splitter and 3 for pratyaya chopper

from sys import argv
from array import *
words=[]
file_write=[]
indict=[]
import correct_sandhi_mod
from correct_sandhi_mod import *
import word_roman_mod
from word_roman_mod import *
import add_word_mod
from add_word_mod import *
import pratyaya_chopper_driver_mod
from pratyaya_chopper_driver_mod import *
import prefix_suffix_mod
from prefix_suffix_mod import *
import os
import init_sandhi_mod
from init_sandhi_mod import *

import sandhi_splitter_driver_mod
from sandhi_splitter_driver_mod import *

import spell_check_driver_mod
from spell_check_driver_mod import *

import prefix_dictionary
from prefix_dictionary import *

import suffix_dictionary
from suffix_dictionary import *

import dawg
#variable for words originally in the dictionary that is copied
#find_this="ಪದ)"
#find_other="/"
remove_numbers=["೧", "೨", "೩", "೪","೫","೬","೭","೮","೯","1","2","3","4","5","6","7","8","9","0"]
remove_chars=["(",")",".",",",";","]","[","}","{",":","!","@","#","$","%","^","&","*","'","/","?","`","~","+","-","=","\"","|","<",">","\\"]
#input_file=input("Please enter the input file name\n")
#in_file = open(input_file, "r")
#first=0
def prepare_file(given_input,mode,prnt_res):
	found_print=[]
	found_print.append(0)
	found_print.append("")
	found_print.append("")
	found_print.append("")
	file_path=given_input.split('/')
	file_name=file_path[-1]
	file_write=[]
	in_file=open(file_name,"r")
	i=0
	if prnt_res==3:
		#if mode==1:
		#elif mode==2:
		#elif mode==3: 
		found_print=[]
		found_print.append(0)
		found_print.append("")
		found_print.append("")
		found_print.append("")
		file_path=given_input.split('/')
		file_name=file_path[-1]
		in_file=open(file_name,"r")
		i=0
		for line in in_file:
			if line!='\n':
				sentences=line.split(".")
				for sentence in sentences:
					i=i+1
					j=0
					iss=str(i)
					file_write.append("\n["+iss+"] "+sentence+".\n")
					for num in remove_numbers:
						if num in sentence:
							sentence=sentence.replace(num,"")
					for char in remove_chars:
						if char in sentence:
							sentence=sentence.replace(char,"")
					if sentence!="":
						words=sentence.split()
						words=list(set(words))
						for word in words:
							j=j+1
							jss=str(j)
							file_write.append("\n"+jss+". "+word+" :\n")
							print("the word is",word)
							after_pratyaya=pratyaya_chopper(word,0)
							if after_pratyaya[0]==1:
								word=after_pratyaya[1]
								file_write.append(after_pratyaya[2])
							if after_pratyaya[3]==1:
								file_write.append("The word is present in the dictionary! It may not contain a sandhi word!")
							else:
						
							
								found_print=sandhi_splitter(word,1)
								if found_print[0]==0:
									found_print[1]="Sandhi could not be split!"
									selected_suggestions=spell_sandhi_checker(word,0)
									print("spell over")
									prefix_suffix_found_print=prefix_suffix(word,0)
									print("prefix suffix over")
									if prefix_suffix_found_print[0]==1:
										if selected_suggestions=='notthere' or selected_suggestions=='':
											sug=prefix_suffix_found_print[1]
										else:
											sug=selected_suggestions+prefix_suffix_found_print[1]
										ordered_suggests=order_suggests(sug)
										selected_suggestions=select_suggest(ordered_suggests,0)
			
									if selected_suggestions=='notthere':
										#have to put a message box here
										#add=input("ಪೂರ್ವ ಪದ / ಉ ತ್ತರ ಪದಗಳು ಪದಕೋ ಶದಲಿ ಸಿಗದು. ಪದಕೋ ಶಕೆ ನೂತನ ಪದ ಸೇರಿಸುವುದೇ ? y/n :\n")
										#if add=='y':
											#add_word()
									#elif selected=='a':
										#add_word(3)
										print("not there")
									else:
										print("in main:")
										print(selected_suggestions)
										found_print.append(1)
										found_print.append(selected_suggestions)
										found_print.append(prefix_suffix_found_print[0])
										found_print.append(prefix_suffix_found_print[2])
										#found_print=sandhi_splitter(selected,1)
						
								if found_print[0]==1:
									file_write.append(found_print[1])
								if len(found_print)>2:
									if found_print[2]==1:
										file_write.append("Did you mean? :\n")
										file_write.append(found_print[3])
										file_write.append("\n")
									if found_print[4]==1:
										file_write.append(found_print[5])
	else:
		if mode==1:
		#english spell checker
			for line in in_file:
				if line!='\n':
					sentences=line.split(".")
					for sentence in sentences:
						i=i+1
						j=0
						iss=str(i)
						file_write.append("\n["+iss+"] "+sentence+".\n")
						for num in remove_numbers:
							if num in sentence:
								sentence=sentence.replace(num,"")
						for char in remove_chars:
							if char in sentence:
								sentence=sentence.replace(char,"")
						if sentence!="":
							words=sentence.split()
							words=list(set(words))
							for word in words:
								j=j+1
								jss=str(j)
								file_write.append("\n"+jss+". "+word+" :\n")
								after_pratyaya=pratyaya_chopper(word,1)
								if after_pratyaya[0]==1:
									word=after_pratyaya[1]
									file_write.append(after_pratyaya[2])
								found_print=spell_check_eng(word)
								if found_print[0]==1:
									file_write.append(found_print[1])
								if len(found_print[2])>0:
									file_write.append("Did you mean? :\n")
									file_write.append(found_print[2])
									file_write.append("\n")
										
		elif mode==2:
		#english sandhi splitter
			
			for line in in_file:
				if line!='\n':
					sentences=line.split(".")
					for sentence in sentences:
						i=i+1
						j=0
						iss=str(i)
						file_write.append("\n["+iss+"] "+sentence+".\n")
						for num in remove_numbers:
							if num in sentence:
								sentence=sentence.replace(num,"")
						for char in remove_chars:
							if char in sentence:
								sentence=sentence.replace(char,"")
						if sentence!="":
							words=sentence.split()
							words=list(set(words))
							for word in words:
								j=j+1
								jss=str(j)
								file_write.append("\n"+jss+". "+word+" :\n")
								print("the word is",word)
								after_pratyaya=pratyaya_chopper(word,0)
								if after_pratyaya[0]==1:
									word=after_pratyaya[1]
									file_write.append(after_pratyaya[2])
								if after_pratyaya[3]==1:
									file_write.append("The word is present in the dictionary! It may not contain a sandhi word!")
								else:
									found_print=sandhi_splitter_eng(word)
									if found_print[0]==1:
										file_write.append(found_print[1])
									if len(found_print)>2:
										if found_print[2]==1:
											file_write.append("Did you mean? :\n")
											file_write.append(found_print[3])
											file_write.append("\n")
										if found_print[4]==1:
											file_write.append(found_print[5])
		elif mode==3:
			for line in in_file:
				if line!='\n':
					sentences=line.split(".")
					for sentence in sentences:
						i=i+1
						j=0
						iss=str(i)
						file_write.append("\n["+iss+"] "+sentence+".\n")
						for num in remove_numbers:
							if num in sentence:
								sentence=sentence.replace(num,"")
						for char in remove_chars:
							if char in sentence:
								sentence=sentence.replace(char,"")
						if sentence!="":
							words=sentence.split()
							words=list(set(words))
							for word in words:
								j=j+1
								jss=str(j)
								file_write.append("\n"+jss+". "+word+" :\n")
								print("the word is",word)
								after_pratyaya=pratyaya_chopper(word,0)
								if after_pratyaya[0]==1:
									word=after_pratyaya[1]
									file_write.append(after_pratyaya[2])
								if after_pratyaya[3]==0:
									found_print=check_pratyaya(word,1)
									if found_print[0]==1:
										file_write.append(found_print[1])
									if len(found_print[2])>0:
										file_write.append("Did you mean?\n")
										file_write.append(found_print[2])
										file_write.append("\n")
								else:
									file_write.append("The root word is : "+word)
										
	output_file=file_name[:-4]+"_out.txt"
	out_file=open(output_file,"w")
	#file_write=list(set(file_write))
	for word in file_write:
		out_file.write("%s\n" % word)
	print("The file "+output_file+" is generated")
	return output_file
