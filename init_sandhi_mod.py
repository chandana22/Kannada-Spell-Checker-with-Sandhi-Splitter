#Author Akshatha Arodi 
#dtd 10/03/2015 as a part of my major project kannada spell checker with sandhi splitter 

import dawg
from sys import argv
from array import *
import spell_check_mod1
from spell_check_mod1 import *
#holder for the dictionary
dictWords=[]
f = open("dictionary_15k.txt", "r")

#read and append words to dictWords
for line in f:
	dictWords.append(line.strip())

#creating a dawg data structure
dict_dawg = dawg.CompletionDAWG(dictWords)

#sandhi possible places
sandhi_places=['aa','uu','ii','ee','oo','ai','au','ya','yu','yo','ye','va','vu','vo','ve', 'RR', 'aR']

#for aagama and aadeesha
kannada_sandhi_places=['g','b','d','y','v']

lopa_places=['u','i','o','e','a']

prefix_vowels=['a','i','u','R']

suffix_vowels1=['aa','ii','uu','RR','ee','ai','oo','au']
suffix_vowels2=['a','i','u','R','e']
