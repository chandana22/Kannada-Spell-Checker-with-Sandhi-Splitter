import dawg
from sys import argv
from array import *
from Levenshtein import *
import operator
import spell_check_mod1
from spell_check_mod1 import *
import correct_sandhi_mod
from correct_sandhi_mod import *
import add_word_mod
from add_word_mod import *
import word_roman_mod
from word_roman_mod import *
import sandhi_splitter_driver_mod
from sandhi_splitter_driver_mod import *
import spell_check_driver_mod
from spell_check_driver_mod import *
import dawg
import os
import morph_hash3
from morph_hash3 import *

#other pratyayas that could be added are:
#gaLa : deevaalayagaLa
#gooskara : avanigooskara
#kke : deevaalayakke
#eMdu : maaduvudeMdu

#allalli not workig

#same ,prnt_res = 3 for kannada
def pratyaya_chopper(to_chop,prnt_res):
	pratyayas=[]
	if prnt_res==3:
		to_chop=to_roman(to_chop)
		output=''
		selected=''
		correct=0
		morphWords=[]
		file_morph=open("morph_forms.txt","r")
		for line in file_morph:
			morphWords.append(line.strip())
		
		morph_dawg=dawg.CompletionDAWG(morphWords)
		f.close()
		correct_root_word=""
		if to_chop in morph_dawg:
			correct_root_word=k[to_chop]
		#guessing what the suffix might be
		suffix=''
	
		#length of to_chop
		len_to_chop=len(to_chop)
	
		#guessing what the sandhi might be
		sandhi=''
	
		#flag to tell if the pratyaya is chopped
		pratyaya_chopped=0
	
		pratyaya=''
	
		#returning this value
		#0 marker if pratyaya is chopped : 0 not chopped, 1 means chopped
		#1 the root word after chopping the pratyaya
		#2 value to just to know if the word is in the dictionary, as a helper to the sanhdi splitter
		#3 last value to tell what to print 
	
		to_chop_returned=[]
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned[3]=0
		to_print=''
	
		if to_chop.endswith('isu'):
			to_chop=to_chop[:len_to_chop-3]
			suffix='u'
			pratyaya='isu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+suffix)+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('annu'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='u'
			pratyaya='annu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			print("in annu")
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+suffix)+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('iMda'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='u'
			pratyaya='iMda'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			print("in Imdau",sandhi)
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+suffix)+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('ige'):
			to_chop=to_chop[:len_to_chop-3]
			suffix='u'
			pratyaya='ige'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+suffix)+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
			len_to_chop=len(to_chop)
	
		if to_chop.endswith('alli'):
			if to_chop=='allalli':
				to_chop_returned[0]='allalli'
				to_chop_returned[1]=to_chop
				to_chop_returned[2]=""
				to_chop_returned[3]=0
				to_chop_returned[4]=""
				return to_chop_returned	
			to_chop=to_chop[:len_to_chop-4]
			print("alli removed",to_chop)
			suffix='u'
			pratyaya='alli'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+suffix)+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('gaLu'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='a'
			pratyaya='gaLu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi=''
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop)+" + "+to_uni(pratyaya)+"\n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('gaL'):
			print("befoer chop", to_chop)
			to_chop=to_chop[:len_to_chop-3]
			print("entereted here",to_chop)
			suffix='a'
			pratyaya='gaLu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi=''
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop)+" + "+to_uni(pratyaya)+"\n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('Mdiru'):
			to_chop=to_chop[:len_to_chop-5]
			suffix='a'
			pratyaya='aMdiru'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1	
			sandhi=''
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop)+" + "+to_uni(pratyaya)+"\n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('Mdir'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='a'
			pratyaya='aMdiru'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi=''
			to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop)+" + "+to_uni(pratyaya)+"\n"
			len_to_chop=len(to_chop)
		
		if len(to_chop)>1:
			if to_chop[-1]=='y': 
				to_chop=to_chop[:-1]
				sandhi='aagama'
				pratyayas.append('y')
				suffix=''
				to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+suffix)+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
			
			elif to_chop[-1]=='v': 
				to_chop=to_chop[:-1]
				sandhi='aagama'
				pratyayas.append('v')
				suffix=''
				to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+suffix)+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
		
			elif to_chop[-1]=='d':
				to_print="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop+"a")+" + "+to_uni(pratyaya)+" ==> "+to_uni(sandhi)+" ಸಂಧಿ \n"
				to_chop=to_chop[:-1]
				pratyayas.append('d')
				sandhi=''
				suffix=''
				to_print+="ಪ್ರತ್ಯಯ ಛೇದ : "+to_uni(to_chop)+" + "+to_uni("da")+"\n"
	
	
		#removed as nannannu doesnt work	
		#if to_chop[-1]=='n':
		#	to_print="Pratyaya removed : "+to_chop+"a + "+pratyaya+"\n"
		#	to_chop=to_chop[:-1]
		#	sandhi=''
		#	suffix=''
		#	to_print+="Pratyaya removed : "+to_chop+" + na\n"
	
		if sandhi=='loopa':
			if to_chop in dict_dawg:
				to_chop_returned[3]=1
			else:
				to_chop=to_chop+suffix
		
		if correct_root_word!="":
			to_chop=correct_root_word
		to_print+="ಮೂಲ ಪದ : "+to_uni(to_chop)+"\n"
		
		to_chop_returned[0]=pratyaya_chopped
		to_chop_returned[1]=to_chop
		to_chop_returned[2]=to_print
		if to_chop in dict_dawg:
			to_chop_returned[3]=1
			print("in dict")
			print("this in dict",to_chop)
		else:
			to_chop_returned[3]=0
		print("this in dict",to_chop)
		to_chop_returned[4]=pratyayas
		#returning this value
		#0 marker if pratyaya is chopped : 0 not chopped, 1 means chopped
		#1 the root word after chopping the pratyaya
		#2 the stuff to print
		#3 value to just to know if the word is in the dictionary, as a helper to the sanhdi splitter
		#4 the pratyaya that is removed
	
	else:
		output=''
		selected=''
		correct=0
	
		#guessing what the suffix might be
		suffix=''
	
		#length of to_chop
		len_to_chop=len(to_chop)
	
		#guessing what the sandhi might be
		sandhi=''
	
		#flag to tell if the pratyaya is chopped
		pratyaya_chopped=0
	
		pratyaya=''
	
		#returning this value
		#0 marker if pratyaya is chopped : 0 not chopped, 1 means chopped
		#1 the root word after chopping the pratyaya
		#2 value to just to know if the word is in the dictionary, as a helper to the sanhdi splitter
		#3 last value to tell what to print 
	
		to_chop_returned=[]
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned.append("")
		to_chop_returned[3]=0
		to_print=''
		file_morph=open("morph_forms.txt","r")
		morphWords=[]
		for line in file_morph:
			morphWords.append(line.strip())
		
		morph_dawg=dawg.CompletionDAWG(morphWords)
		f.close()
		correct_root_word=""
		if to_chop in morph_dawg:
			correct_root_word=k[to_chop]
			
		
			
		if to_chop.endswith('isu'):
			to_chop=to_chop[:len_to_chop-3]
			suffix='u'
			pratyaya='isu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			to_print+="Pratyaya removed : "+to_chop+suffix+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('annu'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='u'
			pratyaya='annu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			print("in annu")
			to_print+="Pratyaya removed : "+to_chop+suffix+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('iMda'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='u'
			pratyaya='iMda'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			print("in Imdau",sandhi)
			to_print+="Pratyaya removed : "+to_chop+suffix+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('ige'):
			to_chop=to_chop[:len_to_chop-3]
			suffix='u'
			pratyaya='ige'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			to_print+="Pratyaya removed : "+to_chop+suffix+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
			len_to_chop=len(to_chop)
	
		if to_chop.endswith('alli'):
			if to_chop=='allalli':
				to_chop_returned[0]='allalli'
				to_chop_returned[1]=to_chop
				to_chop_returned[2]=""
				to_chop_returned[3]=0
				to_chop_returned[4]=""
				return to_chop_returned	
			to_chop=to_chop[:len_to_chop-4]
			print("alli removed",to_chop)
			suffix='u'
			pratyaya='alli'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			to_print+="Pratyaya removed : "+to_chop+suffix+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('gaLu'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='a'
			pratyaya='gaLu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi=''
			to_print+="Pratyaya removed : "+to_chop+" + "+pratyaya+"\n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('gaL'):
			print("befoer chop", to_chop)
			to_chop=to_chop[:len_to_chop-3]
			print("entereted here",to_chop)
			suffix='a'
			pratyaya='gaLu'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi=''
			to_print+="Pratyaya removed : "+to_chop+" + "+pratyaya+"\n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('Mdiru'):
			to_chop=to_chop[:len_to_chop-5]
			suffix='a'
			pratyaya='aMdiru'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1	
			sandhi=''
			to_print+="Pratyaya removed : "+to_chop+" + "+pratyaya+"\n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('Mdir'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='a'
			pratyaya='aMdiru'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi=''
			to_print+="Pratyaya removed : "+to_chop+" + "+pratyaya+"\n"
			len_to_chop=len(to_chop)
		
		if to_chop.endswith('aagi'):
			to_chop=to_chop[:len_to_chop-4]
			suffix='u'
			pratyaya='aagi'
			pratyayas.append(pratyaya)
			pratyaya_chopped=1
			sandhi='loopa'
			to_print+="Pratyaya removed : "+to_chop+suffix+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
			len_to_chop=len(to_chop)
			
		#if to_chop.endswith('aada'):
		#	to_chop=to_chop[:len_to_chop-4]
		#	suffix='u'
		#	pratyaya='aada'
		#	pratyayas.append(pratyaya)
		#	pratyaya_chopped=1
		#	sandhi='loopa'
		#	to_print+="Pratyaya removed : "+to_chop+suffix+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
		#	len_to_chop=len(to_chop)	
		
		if len(to_chop)>1:
			if to_chop[-1]=='y': 
				to_chop=to_chop[:-1]
				sandhi='aagama'
				pratyayas.append('y')
				suffix=''
				to_print="Pratyaya removed : "+to_chop+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
			
			elif to_chop[-1]=='v': 
				to_chop=to_chop[:-1]
				sandhi='aagama'
				pratyayas.append('v')
				suffix=''
				to_print="Pratyaya removed : "+to_chop+" + "+pratyaya+" ==> "+sandhi+" sandhi \n"
		
			elif to_chop[-1]=='d':
				to_print="Pratyaya removed : "+to_chop+"a + "+pratyaya+" ==> "+sandhi+" sandhi \n"
				to_chop=to_chop[:-1]
				pratyayas.append('d')
				sandhi=''
				suffix=''
				to_print+="Pratyaya removed : "+to_chop+" + da \n"
			
	
	
		#removed as nannannu doesnt work	
		#if to_chop[-1]=='n':
		#	to_print="Pratyaya removed : "+to_chop+"a + "+pratyaya+"\n"
		#	to_chop=to_chop[:-1]
		#	sandhi=''
		#	suffix=''
		#	to_print+="Pratyaya removed : "+to_chop+" + na\n"
	
		if sandhi=='loopa':
			if to_chop in dict_dawg:
				to_chop_returned[3]=1
			else:
				to_chop=to_chop+suffix
		
		if correct_root_word!="":
			to_chop=correct_root_word
			pratyaya_chopped=1
			
		to_print+="The root word: "+to_chop+"\n"
		to_chop_returned[0]=pratyaya_chopped
		to_chop_returned[1]=to_chop
		to_chop_returned[2]=to_print
		if to_chop in dict_dawg:
			to_chop_returned[3]=1
			print("in dict")
			print("this in dict",to_chop)
		else:
			to_chop_returned[3]=0
		print("this in dict",to_chop)
		to_chop_returned[4]=pratyayas
		#returning this value
		#0 marker if pratyaya is chopped : 0 not chopped, 1 means chopped
		#1 the root word after chopping the pratyaya
		#2 the stuff to print
		#3 value to just to know if the word is in the dictionary, as a helper to the sanhdi splitter
		#4 the pratyaya that is removed
	
	return to_chop_returned
	

def check_pratyaya(to_chop,prnt_res):
	if prnt_res==3:
		correct_selected=spell_check_kan(to_uni(to_chop))
	else:
		correct_selected=spell_check_eng(to_chop)	

	return correct_selected
