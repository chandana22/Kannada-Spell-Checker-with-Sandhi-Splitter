#Adding words to the dictionary
#Author Akshatha dtd 14/03/15
#modified to support the GUI on 03/04/15

import dawg
from sys import argv
from array import *
import spell_check_mod1
from spell_check_mod1 import *

def check_indict(word):
	#read and append words to dictWords
	f = open("dictionary_15k.txt", "r")
	rf = open("reverse_dictionary_15k.txt", "r")
	
	for line in f:
		dictWords.append(line.strip())

	#creating a dawg data structure
	dict_dawg = dawg.CompletionDAWG(dictWords)
	if word in dict_dawg:
		return 1
	return 0

def add_word(word,prnt_res):
	f = open("dictionary_15k.txt", "a")
	rf = open("reverse_dictionary_15k.txt", "a")
	if prnt_res==3:
		word=to_roman(word)
	found=check_indict(word)
	if found==0:
		f.write("%s\n" % word)
		rf.write("%s\n" % word[::-1])
	f.close()
	rf.close()
	f = open("dictionary_15k.txt", "r")

	#read and append words to dictWords
	for line in f:
		dictWords.append(line.strip())
	dict_dawg = dawg.CompletionDAWG(dictWords)
	
	f.close()
	return 1
