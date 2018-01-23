#Author Akshatha A N dtd 12/04/15 

#found_print[0] if sandhi is found or not
#found_print[1] has suggestions
#found_print[2] has what sandhis are made of

import init_sandhi_mod
from init_sandhi_mod import *

import prefix_dictionary
from prefix_dictionary import *

import suffix_dictionary
from suffix_dictionary import *

import word_roman_mod
from word_roman_mod import *

import dawg


def prefix_suffix(given_word,prnt_res):
	i=2
	prefix_match=''
	suffix_match=''
	
	prefix_dawg=dawg.CompletionDAWG(prefix_removed)
	suffix_dawg=dawg.CompletionDAWG(suffix_removed)
	len_given_word=len(given_word)
	while i<len_given_word:
		prefix_check_word=given_word[:i]
		if prefix_check_word in prefix_dawg:
			prefix_match=prefix_check_word
		i=i+1		
	i=2
	while i<len_given_word:
		suffix_check_word=given_word[len_given_word-i:len_given_word]
		if suffix_check_word in suffix_dawg:
			suffix_match=suffix_check_word
		i=i+1
	if prefix_match!='' and suffix_match!='':
		print("printing prefix match")
		print(prefix_match)
		print(prefix_map[prefix_match])
		print("printing suffix match")
		print(suffix_match)
		print(suffix_map[suffix_match])
	
		return sandhi_maker(prefix_match,suffix_match,len_given_word,prnt_res)
	else:
		found_print=[]
		found_print.append(0)
		found_print.append('')
		found_print.append('')
		return found_print

	#reverse rule base t make sandhi
def sandhi_maker(prefix_match,suffix_match,len_given_word,prnt_res):
	found_print=[]
	k_sandhi_words=[]
	found_print.append(0)
	found_print.append("")
	if prnt_res==3:
		found_print.append("ಸಂಧಿಯಲ್ಲಿ ತಪ್ಪಾದಂತಿದೆ!\nಸಂಧಿಯ ಮಾಹಿತಿ ಇಂತಿದೆ  : \n")
	else:
		found_print.append("The given word may contain a sandhi mistake!\nUsing sandhi maker, generating suggestions.\nSandhi refernce for suggestions : \n")
	sandhi_words=[]
	found=0
	
	for prefix_last in prefix_map[prefix_match]:
		print("prefix last",prefix_last)
		for suffix_first in suffix_map[suffix_match]:
			
			if prefix_last=='a' and (suffix_first=='a' or suffix_first=='aa'):
				sandhi_place='aa'
				sandhi_word=prefix_match+sandhi_place+suffix_match
				sandhi="savarNadiirgha"				
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
						
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			elif prefix_last=='i' and (suffix_first=='i' or suffix_first=='ii'):
				sandhi_place='ii'
				sandhi_word=prefix_match+sandhi_place+suffix_match
				sandhi="savarNadiirgha"
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			elif prefix_last=='u' and (suffix_first=='u' or suffix_first=='uu'):
				sandhi_place='uu'
				sandhi_word=prefix_match+sandhi_place+suffix_match
				sandhi="savarNadiirgha"
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			elif prefix_last=='R' and (suffix_first=='R' or suffix_first=='RR'):
				sandhi_place='RR'
				sandhi_word=prefix_match+sandhi_place+suffix_match
				sandhi="savarNadiirgha"
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			elif prefix_last=='a' and (suffix_first=='i' or suffix_first=='ii'):
				sandhi_place='ee'
				sandhi_word=prefix_match+sandhi_place+suffix_match
				sandhi="savarNadiirgha"
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					print("setting one")
					found=1
			
			elif prefix_last=='a' and (suffix_first=='u' or suffix_first=='uu'):
				sandhi_place='oo'
				sandhi="guNa"
				print("in guNa")
				sandhi_word=prefix_match+sandhi_place+suffix_match
				print("sandh word",sandhi_word)
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			
			elif prefix_last=='a' and (suffix_first=='R' or suffix_first=='RR'):
				sandhi_place='aR'
				sandhi="guNa"
				sandhi_word=prefix_match+sandhi_place+suffix_match
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			elif prefix_last=='a' and (suffix_first=='ee' or suffix_first=='ai'):
				sandhi_place='ai'
				sandhi="vruddhi"
				sandhi_word=prefix_match+sandhi_place+suffix_match
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			elif prefix_last=='a' and (suffix_first=='oo' or suffix_first=='au'):
				sandhi_place='au'
				sandhi="vruddhi"
				sandhi_word=prefix_match+sandhi_place+suffix_match
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			elif prefix_last=='i' and (suffix_first=='a' or suffix_first=='u' or suffix_first=='o' or suffix_first=='e'):
				sandhi_place='y'
				print("in i")
				sandhi="yaN"
				sandhi_word=prefix_match+sandhi_place+suffix_first+suffix_match
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			if (prefix_last=='u' or prefix_last=='v') and (suffix_first=='a' or suffix_first=='i' or suffix_first=='o' or suffix_first=='e'):
				sandhi_place='v'
				sandhi="yaN"
				sandhi_word=prefix_match+sandhi_place+suffix_first+suffix_match
				if len(sandhi_word)>len_given_word-1:
					sandhi_words.append(sandhi_word)
					if prnt_res==3:
						found_print[2]+=to_uni(prefix_match+prefix_last)+" + "+to_uni(suffix_first+suffix_match)+" = "+to_uni(sandhi_word)+" == > "+to_uni(sandhi)+"\n"
						k_sandhi_words.append(to_uni(sandhi_word))
					else:
						found_print[2]+=prefix_match+prefix_last+" + "+suffix_first+suffix_match+" = "+sandhi_word+" == > "+sandhi+"\n"
					found=1
			
			if found==1:
				found_print[0]=1
				if prnt_res==3:
					sandhi_words=k_sandhi_words				
				found_print[1]=sandhi_words
				print("printing sandhi words")
				print(sandhi_words)
				print("in one")
			else:
				found_print[0]=0
				found_print[1]='notthere'
				found_print[2]=""
								
	
	
	return found_print

#while(1):
#	given_word=input("enter word to check")
#	found_print=prefix_suffix(given_word,0)
#	print("found_print[0] ",found_print[0])
#	print("found_print[1] ",found_print[1])
#	print("found_print[2] ",found_print[2])
	
