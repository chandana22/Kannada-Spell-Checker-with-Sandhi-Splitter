#Author Akshatha Arodi dtd 02/04/15
#this is a driver written to connect to the GUI
#I am putting stuff in a main function to call all stuff

#found_print[0] if the sandhi is handled.
#found_print[1] suggestiions or whatever to print
#found_print[2] if spell_something with suggestions are generated is called 0 not called 1 called
#found_print[3] all suggestions
#found_print[4] if prefix suffix is called 0 not called 1 called
#found_print[5] whatever prefix suffix wants to print

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

import prefix_dictionary
from prefix_dictionary import *

import suffix_dictionary
from suffix_dictionary import *

import dawg

#everything in kannada as the user knows kannada
#if input_encoding=='1':
def sandhi_splitter_kan(uni_word):
	roman_word=to_roman(uni_word)
	# 3 to print in kannada
		#roman_word=to_roman(uni_word)
	# 3 to print in kannada
	sug1=[]
	global found_print
	found_print=[]
	found_print.append(0)
	found_print.append("")
	found_print.append("")
	found_print.append("")
	print("the word is",roman_word)
	found_print=sandhi_splitter(roman_word,3)
	if found_print[0]==0:
		found_print[1]="ಸಂಧಿ ಪದ ಛೇದ ಆಗದು!!"
		selected_suggestions=spell_sandhi_checker(roman_word,3)
		print("spell over")
		prefix_suffix_found_print=prefix_suffix(roman_word,3)
		print("prefix suffix over")
		if prefix_suffix_found_print[0]==1:
			if selected_suggestions=='notthere' or selected_suggestions=='':
				sug=prefix_suffix_found_print[1]
				for y in sug:
					sug1.append(to_roman(y))
				sug=sug1
			else:
			#coz pre suf is returning in kannada
				
				sug=selected_suggestions+prefix_suffix_found_print[1]
				print("printin pre")
				print(prefix_suffix_found_print[1])
				print("printin sel")
				print(selected_suggestions)
				print(sug)
				for y in sug:
					sug1.append(to_roman(y))
				sug=sug1
				#	selected_suggestions.append(to_roman(y))
			ordered_suggests=order_suggests(sug)
			print("ordered")
			print(ordered_suggests)
			selected_suggestions=select_suggest(ordered_suggests,3)
			print("sel")
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
	
	return found_print
	#ans=input("\nಪುನಃ ಸಂಧಿ ಛೇಧಿಸಲು ಬಯ ಸು ವಿರಾ ?  y/n : ")

#everything in english
def sandhi_splitter_eng(word):
	#roman_word=to_roman(uni_word)
	# 3 to print in kannada
	global found_print
	found_print=[]
	found_print.append(0)
	found_print.append("")
	found_print.append("")
	found_print.append("")
	print("the word is",word)
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
	
	return found_print
	#ans=input("\nಪುನಃ ಸಂಧಿ ಛೇಧಿಸಲು ಬಯ ಸು ವಿರಾ ?  y/n : ")
	
