#Author Akshatha Arodi 
#dtd 10/03/2015 as a part of my major project kannada spell checker with sandhi splitter 
#found_print[0] 0 if sandhi not found 1 if found
#found_print[1] gives what to be printed if sandhi is found
#found_print[1] has suggestions otherwise ( if in spell_ something
#initialised
#lookaika bug fixed
import init_sandhi_mod
from init_sandhi_mod import *
import word_roman_mod
from word_roman_mod import *
import spell_check_mod1
from spell_check_mod1 import *
global selected
global dict_dawg
global rev_dict_dawg
global prnt_res

#I need to return a flag saying if the thing is found or not, also if found what to print. 
#So, I am using an array called found_print


def init_dawg():
	global dict_dawg
	global rev_dawg
	f = open("dictionary_15k.txt", "r")
	for line1 in f:
		dictWords.append(line1.strip())

#read the store the reverse dictionary
	rev_f=open("reverse_dictionary_15k.txt","r")
	for line in rev_f:
		rev_dictWords.append(line.strip())
				
#creating the reverse dawg
	rev_dict_dawg=dawg.CompletionDAWG(rev_dictWords)
	dict_dawg=dawg.CompletionDAWG(dictWords)
	
	
#spell checker with sandhi splitter module
def spell_sandhi_checker(given_word,prnt_res):
	global found_print
	found_print=[]
	found_print.append(0)
	found_print.append("")
	found_print.append("")
	found_print.append("")
	called_sandhi_maker=0
	i=2
	init_dawg()
	found=0
	found_print[0]=found
	given_word_len=len(given_word)
	global selected
	selected=''
	global spell_done
	spell_done=0
	while i<given_word_len:
		check_word=given_word[:i]
	
		#need to make lopa leave the word for a few combinations		
		#lopa_exclude=given_word[i]
	
		last=check_word[-1]
	
		#exclude this in lopa sandhi : skip the check
		#lopa_leave=last+lopa_exclude
	
		lastbone=check_word[-2]
		guessed_sandhi_place=lastbone+last
		
		#guessed_sandhi_place=check_word[-3:-1]
		if guessed_sandhi_place in sandhi_places:
			guessed_prefix=check_word[:-2]
			guessed_suffix=given_word[i:]
			
			#call a function to check the sandhi
			found_print=check_sandhi(guessed_prefix,guessed_suffix,guessed_sandhi_place,1,prnt_res)
		i=i+1
	i=2
	while i<given_word_len:
		check_word=given_word[:i]		
		last=check_word[-1]
		if found_print[0]==0 and last in kannada_sandhi_places:
			kannada_prefix=check_word[:-1]
			guessed_suffix=given_word[i:]
			found_print=spell_check_kannada_sandhi(kannada_prefix,guessed_suffix,last,prnt_res)
				
		i=i+1
	
	#checking and generation lopa sandhi places
	#This is generating a lot of unwanted suggestions
	#i=1
	#while i<given_word_len and found_print[0]!=1:
	#	lopa_len=given_word_len-i
	#	lopa_suffix=given_word[lopa_len:given_word_len]
	#	lopa_prefix=given_word[:lopa_len]
	#	found_print=spell_check_lopa_sandhi(lopa_prefix,lopa_suffix,prnt_res)
	#	i=i+1
	print("this is what sepll sandhi checker is returning")
	print(found_print[1])
	return found_print[1]
#removed stuff from here
	
#checking for valid sandhi with spell checker
def spell_valid_sandhi(guessed_prefix,guessed_suffix,sandhi_name,prefix_last,suffix_first1,suffix_first2,sandhi_place,prnt_res):
	found=0
	#found_print=[]
	#found_print.append(0)
	#found_print.append("")
	prefix=guessed_prefix+prefix_last
	sandhi=sandhi_name
	prefix_suggests=[]
	suffix_suggests=[]
	
	if prefix in dict_dawg:
		print("prefix in dict dawg")
	#prefix is already found in the word. So guess only sufffix
		prefix_suggests.append(guessed_prefix)
		suffix=suffix_first1+guessed_suffix
		
		#guess all the words which begin with the first suffix word
		suffix1_suggests=spell_check(suffix,'f',suffix_first1)
		print("before chop")
		print(suffix1_suggests)
		suffix_first1_len=len(suffix_first1)
		for word in suffix1_suggests:
			suffix_suggests.append(word[suffix_first1_len:])
		print("first time suffix suggests")
		print(suffix_suggests)
			
		suffix=suffix_first2+guessed_suffix
		suffix2_suggests=spell_check(suffix,'f',suffix_first2)
		suffix_first2_len=len(suffix_first2)
		for word in suffix2_suggests:
			suffix_suggests.append(word[suffix_first2_len:])
		print("secnd time suffix suggests")
		print(suffix_suggests)
		suffix_suggests=list(set(suffix_suggests))
		print("suf suggest")
		print(suffix_suggests)
		if len(suffix_suggests) > 0:
			found=1

	if suffix_first1+guessed_suffix in dict_dawg or suffix_first2+guessed_suffix in dict_dawg:		
		prefix_suggests1=spell_check(prefix[::-1],'r',prefix_last)
		suffix_suggests.append(guessed_suffix)
		print("suffix found")
		for word in prefix_suggests1:
			w=word[::-1]
			prefix_suggests.append(w[:-1])
		if len(prefix_suggests)>0:
			found=1
	print("saw for suf")	
	if found==1:
		print("insude founf=1")
		found_print[0]=found
		found_print[1]=spell_print_result(prefix_suggests,suffix_suggests,sandhi,sandhi_place,prnt_res)
	#found_print[0]=found
	print("printing found_print11")
	print(found_print)
	return found_print

#the combintions of all prefix and suffixes and sandhis to be printed

def spell_print_result(prefix_suggests,suffix_suggests,sandhi,sandhi_place,prnt_res):
	global selected
	given_suggests=[]
	for prefix in prefix_suggests:
		for suffix in suffix_suggests:
			word=prefix+sandhi_place+suffix
			given_suggests.append(word)
			
	ordered_suggests=order_suggests(given_suggests)
	return select_suggest(ordered_suggests,prnt_res)
	#print_suggestions(prnt_res)

#checking kannada sandhi will spell checker
def spell_check_kannada_sandhi(prefix,guessed_suffix,last,prnt_res):
	found=0
	found_print=[]
	found_print.append(0)
	found_print.append("")
	prefix_suggests=[]
	suffix_suggests=[]
	if last=='g':
		suffix='k'+guessed_suffix
		sandhi="Aadeesha"
	elif last=='d':
		suffix='t'+guessed_suffix
		sandhi="Aadeesha"
	elif last=='b':
		suffix='p'+guessed_suffix
		sandhi="Aadeesha"
	elif last=='y':
		suffix=guessed_suffix
		sandhi="Aagama"
	elif last=='v':
		suffix=guessed_suffix
		sandhi="Aagama"
	if prefix in dict_dawg:
		prefix_suggests.append(prefix)			
		suffix_suggests1=spell_check(suffix,'f',suffix[0])
		for w in suffix_suggests1:
			word=w[1:]
			suffix_suggests.append(word)
		if len(suffix_suggests)>0:
			found=1
			
	elif suffix in dict_dawg:
		suffix_suggests.append(guessed_suffix)
		prefix_suggests=spell_check(prefix,'f','')
		if len(prefix_suggests)>0:
			found=1
	if found==1:
		found_print[1]=spell_print_result(prefix_suggests,suffix_suggests,sandhi,last,prnt_res)
	found_print[0]=found
	return found_print


#checking lopa sandhi with spelling 
def spell_check_lopa_sandhi(lopa_prefix,lopa_suffix,prnt_res):
	found=0
	found_print=[]
	found_print.append(0)
	found_print.append("")
	suffix_begin=lopa_suffix[0]
	possible_prefix=[]
	suffix_suggests=[]
	prefix_suggests=[]
	if lopa_suffix in dict_dawg:
		suffix_suggests.append(lopa_suffix)
		for vowel in lopa_places:
			prefix=lopa_prefix+vowel
			prefix_suggests+=spell_check(prefix,'f','')
	else:
		for vowel in lopa_places:
			prefix=lopa_prefix+vowel
			if prefix in dict_dawg:
				prefix_suggests.append(prefix)
				suffix_suggests+=spell_check(lopa_suffix,'f','')
	if len(prefix_suggests)>0 or len(suffix_suggests)>0:
		found=1
		
	

	if found==1:
		prefix1_suggests=[]
		for w in prefix_suggests:
			prefix1_suggests.append(w[:-1])
		found_print[1]=spell_print_result(prefix1_suggests,suffix_suggests,'loopa','',prnt_res)	
	found_print[0]=found
	return found_print

#main sandhi splitter module that tells if the word is split properly
#takes the word as input and a bool prnt_res  such as prnt : 0 no printing result prnt :1 prints result
def sandhi_splitter(given_word,prnt_res):
	found_print=[]
	found_print.append(0)
	found_print.append("")
	given_word_len=len(given_word)
	
	i=2
	found=0
	found_print[0]=found
	check_word=''
	#refresh dawg after adding the words
	init_dawg()
	#this to show the word is swept for suggestions
	global done
	done=0
	while found_print[0]==0 and i<given_word_len:
		
		check_word=given_word[:i]
		
		#need to make lopa leave the word for a few combinations		
		#lopa_exclude=given_word[i]
		
		last=check_word[-1]
		
		#exclude this in lopa sandhi : skip the check
		#lopa_leave=last+lopa_exclude
		
		lastbone=check_word[-2]
		guessed_sandhi_place=lastbone+last
		
		if guessed_sandhi_place in sandhi_places:
			guessed_prefix=check_word[:-2]
			guessed_suffix=given_word[i:]
			
			#call a function to check the sandhi
		
			found_print=check_sandhi(guessed_prefix,guessed_suffix,guessed_sandhi_place,0,prnt_res)
	
		
		if found_print[0]!=1 and last in kannada_sandhi_places:
			kannada_prefix=check_word[:-1]
			guessed_suffix=given_word[i:]
			found_print=check_kannada_sandhi(kannada_prefix,guessed_suffix,last,prnt_res)
		i=i+1
		
		#checking lopa sandhi
	i=1
	while i<given_word_len and found_print[0]!=1:
		lopa_len=given_word_len-i
		lopa_suffix=given_word[lopa_len:given_word_len]
		lopa_prefix=given_word[:lopa_len]
		found_print=check_lopa_sandhi(lopa_prefix,lopa_suffix,prnt_res)
		i=i+1
	done=1
	return found_print
	
#function to check the sandhi
#spell=0 indicates spell checker mode is off

def check_sandhi(guessed_prefix,guessed_suffix,guessed_sandhi_place,spell,prnt_res):
	#first see if the word itself has the splits	
	#see the possible cases
	
	found=0
	# savarNadiirgha aa= a+a/aa
	if guessed_sandhi_place=='aa':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'a','a','aa',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'a','a','aa','aa',prnt_res)
			
	# savarNadiirgha ii= i+i/ii
	elif guessed_sandhi_place=='ii':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'i','i','ii',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'i','i','ii','ii',prnt_res)
	
	# savarNadiirgha uu= u+u/uu
	elif guessed_sandhi_place=='uu':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'u','u','uu',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'u','u','uu','uu',prnt_res)	
	
	# savarNadiirgha RR= R+R/RR
	elif guessed_sandhi_place=='RR':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'R','R','RR',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"savarNadiirgha",'R','R','RR','RR',prnt_res)
		
	# guna sandhi oo=a+u/uu
	elif guessed_sandhi_place=='oo':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"guNa",'a','u','uu',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"guNa",'a','u','uu','oo',prnt_res)	
			
	# guna sandhi ee=a+i/ii
	elif guessed_sandhi_place=='ee':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"guNa",'a','i','ii',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"guNa",'a','i','ii','ee',prnt_res)	
					
	# guna sandhi aR=a+R/RR
	elif guessed_sandhi_place=='aR':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"guNa",'a','R','RR',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"guNa",'a','R','RR','aR',prnt_res)	
			
	# vruddhi sandhi a+ee/ai = ai
	elif guessed_sandhi_place=='ai':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"vruddhi",'a','ee','ai',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"vruddhi",'a','ee','ai','ai',prnt_res)
			print("in vrudhi")
			print("pre",guessed_prefix)
			print("suf",guessed_suffix)	
				
	# vruddhi sandhi a+oo/au = au
	elif guessed_sandhi_place=='au':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"vruddhi",'a','oo','au',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"vruddhi",'a','oo','au','au',prnt_res)
		
	
	# yan ya=i+a/aa
	elif guessed_sandhi_place=='ya':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','a','aa',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','a','aa','ya',prnt_res)
	
	# yan yu=i+u/uu
	elif guessed_sandhi_place=='yu':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','u','uu',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','u','uu','yu',prnt_res)
	
	# yan yo=i+o/oo
	elif guessed_sandhi_place=='yo':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','o','oo',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','o','oo','yo',prnt_res)
	
	# yan ye=i+e/ee
	elif guessed_sandhi_place=='ye':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','e','ee',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'i','e','ee','ye',prnt_res)
		
	# yan va=v+a/aa
	elif guessed_sandhi_place=='va':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','a','aa',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','a','aa','va',prnt_res)
	
	# yan vu=u+i/ii
	elif guessed_sandhi_place=='vu':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','i','ii',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','i','ii','vu',prnt_res)
	
	# yan vo=u+o/oo
	elif guessed_sandhi_place=='vo':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','o','oo',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','o','oo','vo',prnt_res)
	
	# yan ve=u+e/ee
	elif guessed_sandhi_place=='ve':
		if spell==0:
			found_print=valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','e','ee',prnt_res)
		else:
			found_print=spell_valid_sandhi(guessed_prefix,guessed_suffix,"yaN",'u','e','ee','ve',prnt_res)
	
	return found_print

#putting the sandhi finding process in one function
def valid_sandhi(guessed_prefix,guessed_suffix,sandhi_name,prefix_last,suffix_first1,suffix_first2, prnt_res):
	found=0
	prefix=guessed_prefix+prefix_last
	sandhi=sandhi_name
	found_print=[]
	found_print.append(0)
	found_print.append("")
	if prefix in dict_dawg:
	#see ex a=a+a
		suffix=suffix_first1+guessed_suffix
		if suffix in dict_dawg:		
				found=1
		else:
			suffix=suffix_first2+guessed_suffix
			if suffix in dict_dawg:		
				found=1
			else:
				found=0
	if found==1 and prnt_res==1:
		#make found and 
		found_print[0]=found
		found_print[1]=print_result(prefix,suffix,sandhi)
	#customised for spell checker
	
	
	
	
	#need to fix this
	elif found==1 and prnt_res==2:
		found_print[0]=found
		to_print="\n"+sandhi+" sandhi"+" => "+prefix+" + "+suffix
		found_print[1]=to_print
	
	#prnt_res =4 means print a short form of the sandhi in kannada
	elif found==1 and prnt_res==4:
		found_print[0]=found
		sandhi=to_uni(sandhi)
		prefix=to_uni(prefix)
		suffix=to_uni(suffix)
		to_print="\n"+sandhi+" ಸಂಧಿ "+" => "+prefix+" + "+suffix
		found_print[1]=to_print
		
	#customised for kannada interface
	elif found==1 and prnt_res==3:
		to_print="\nಸಂಧಿ ಪದ ಛೇದ ಸಫಲವಾಗಿದೆ.\n"
		sandhi=to_uni(sandhi)
		prefix=to_uni(prefix)
		suffix=to_uni(suffix)
		
		to_print+="ಪೂರ್ವ ಪದ     :   "+prefix+"\n"
		to_print+="ಉತ್ತರ ಪದ       :   "+suffix+"\n"
		to_print+="ಸಂಧಿ                :   "+sandhi+"\n"
		found_print[1]=to_print
	found_print[0]=found
	
	return found_print


#checking kannada sandhis
def check_kannada_sandhi(prefix,guessed_suffix,last,prnt_res):
	found=0
	found_print=[]
	found_print.append(0)
	found_print.append("")
	if prefix=='kaM':
		prefix='kaN'
	if prefix in dict_dawg:
		if last=='g':
			suffix='k'+guessed_suffix
			sandhi="aadeesha"
		elif last=='d':
			suffix='t'+guessed_suffix
			sandhi="aadeesha"
		elif last=='b':
			suffix='p'+guessed_suffix
			sandhi="aadeesha"
		elif last=='y':
			suffix=guessed_suffix
			sandhi="aagama"
		elif last=='v':
			suffix=guessed_suffix
			sandhi="aagama" 
		if suffix in dict_dawg:
			if prnt_res==3:
				to_print="\nಸಂಧಿ ಪದ ಛೇದ ಸಫಲವಾಗಿದೆ.\n"
				sandhi=to_uni(sandhi)
				prefix=to_uni(prefix)
				suffix=to_uni(suffix)
		
				to_print+="ಪೂರ್ವ ಪದ     :   "+prefix+"\n"
				to_print+="ಉತ್ತರ ಪದ       :   "+suffix+"\n"
				to_print+="ಸಂಧಿ                :   "+sandhi+"\n"
				found_print[1]=to_print
			elif prnt_res==4:
				found_print[0]=found
				sandhi=to_uni(sandhi)
				prefix=to_uni(prefix)
				suffix=to_uni(suffix)
				found_print[1]="\n"+sandhi+" ಸಂಧಿ "+" => "+prefix+" + "+suffix
			elif prnt_res==2:
				found_print[0]=found
				to_print="\n"+sandhi+" sandhi"+" => "+prefix+" + "+suffix
				found_print[1]=to_print
			else:
				found_print[1]=print_result(prefix,suffix,sandhi)
			found=1
			
	found_print[0]=found
	return found_print

#find lopa 
def check_lopa_sandhi(lopa_prefix,lopa_suffix,prnt_res):
	found=0
	found_print=[]
	found_print.append(0)
	found_print.append("")
	found_print[0]=0
	suffix_begin=lopa_suffix[0]
	possible_prefix=[]
	if lopa_suffix in dict_dawg:
		for vowel in lopa_places:
			prefix=lopa_prefix+vowel
			if prefix in dict_dawg:
				if prnt_res==3:
					to_print="\nಸಂಧಿ ಪದ ಛೇದ ಸಫಲವಾಗಿದೆ.\n"
					sandhi='loopa'
					sandhi=to_uni(sandhi)
					prefix=to_uni(prefix)
					suffix=to_uni(lopa_suffix)
		
					to_print+="ಪೂರ್ವ ಪದ     :   "+prefix+"\n"
					to_print+="ಉತ್ತರ ಪದ       :   "+suffix+"\n"
					to_print+="ಸಂಧಿ                :   "+sandhi+"\n"
					found_print[1]=to_print
				elif prnt_res==4:
					found_print[0]=found
					sandhi='loopa'
					sandhi=to_uni(sandhi)
					prefix=to_uni(prefix)
					suffix=to_uni(lopa_suffix)
					found_print[1]="\n"+sandhi+" ಸಂಧಿ "+" => "+prefix+" + "+suffix
				elif prnt_res==2:
					found_print[0]=found
					to_print="\nloopa sandhi"+" => "+prefix+" + "+lopa_suffix
					found_print[1]=to_print
				else:
					found_print[1]=print_result(prefix,lopa_suffix,"loopa")
				found_print[0]=1
				return found_print
	return found_print
		

#defining printing result
def print_result(prefix,suffix,sandhi):
	to_print="\nSandhi is successfully split!\n\n"
	to_print+="Puurvapada  :   "+prefix+"\n"
	to_print+="Uttarapada   :   "+suffix+"\n"
	to_print+="Sandhi            :   "+sandhi+"\n"
	return to_print

