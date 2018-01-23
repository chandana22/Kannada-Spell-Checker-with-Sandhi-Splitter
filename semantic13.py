import os
import dawg
from sys import argv
from array import *
from Levenshtein import *
import operator
import word_roman_mod
from word_roman_mod import *
import init_sandhi_mod
from init_sandhi_mod import *

def semantic(given_word,prnt_res):
	if prnt_res==3:
		
		list1=[]
			    
		diccy= open("hello_stripped.txt", "r")
		morphology= open("morphology1.txt", "r")
		to_the_file=[]	
		lines=diccy.readlines()
		dictionaryWords=[]		
		d=0
		correct_input=""
		
		for line in morphology:
			dictionaryWords.append(line)

		#putting each word in list
		for a in range(0,305570):
			dictionaryWords.append(dictionaryWords[a].strip())

		completion_dawg = dawg.CompletionDAWG(dictionaryWords)
		#print(given_word)
		to_the_file.append(given_word)
		word = given_word.split()
		pronoun_value=""
		verb=0
		noun=0
		tag_pronoun=""
		noun_value=""
		tag_noun=""
		pronoun=0
		found=0
		flag=0
		tag_verb=""
		for letter in word:
			suggest_word=[]
			suggest_line=[]
			ret_list=[]
			letter=to_roman(letter)
			if letter not in completion_dawg:
				for inflection in dictionaryWords:
					d=distance(letter,inflection)
					if d<2:
						suggest_word.append(inflection)
				if suggest_word:
					
					suggest_word=list(set(suggest_word))
					for suggestion in suggest_word:
						suggest_line.append(given_word.replace(to_uni(letter),to_uni(suggestion)))
					ret_list.append(0)
					ret_list.insert(1,"ಈ ವಾಕ್ಯದ ಪದಬರಿಗೆಯಲ್ಲಿ ತಪ್ಪಿದೆ!")
					ret_list.insert(2, suggest_line)
					return ret_list
			nlines=0
			for line in lines:
				nlines += 1
			
				if(((letter+"\n")==line)==True):
		
					line_no=nlines
		
					if noun_value!="" and flag==0:
						tag_noun=lines[nlines]
											
						flag=1
						noun=1
					if flag==1 and (line[:-1].endswith(('iMda','u'))==True) and lines[nlines].startswith('N'):
						tag_noun=""
						noun_value=""
						flag=0
						noun=0
					if (lines[nlines].startswith('N') and noun==0 and (line[:-1].endswith(('iMda','u'))==True) and (line[:-1].endswith('annu')==False) and noun_value==""):
								
						#to_the_file.append("ನಾಮಪದವು "+letter)
										
						tag_noun=lines[nlines]
				
						noun=1
					elif ((lines[nlines].startswith('ITER') or lines[nlines].startswith('PROG') or lines[nlines].startswith('ABS'))):
						
						#to_the_file.append("ಕ್ರಿಯಾಪದವು  " +lines[nlines-1])					
	
						tag_verb=lines[nlines]
						verb=1
					elif(lines[nlines].startswith('PRO') and pronoun==0):
								
						
						pronoun_value=lines[nlines-1]
						if pronoun_value[:-1]=="nanna":
							number=word.index(letter)+1
							noun_value=word[number]
							
							if noun_value not in dict_dawg:
								noun_value=""
							
						#to_the_file.append("ಆಡುಗಪದವು " +lines[nlines-1])	
						
						tag_pronoun=lines[nlines]
						pronoun=1
											
				if (noun==1 and verb==1):
					break;
		nlines=line_no
		if ((tag_pronoun=="")==False) and (tag_noun==""):
			tag_noun=tag_pronoun
			noun=pronoun
		if verb==0 or noun==0:
			found=1
		ret_list.insert(0,1)	
	
		if ('PAST' in tag_verb):
			
			to_the_file.append("ಇದು ಭೂತಕಾಲ ವಾಕ್ಯ  ")
		elif ('PRES' in tag_verb):
			
			to_the_file.append("ಇದು ವರ್ತಮಾನಕಾಲ ವಾಕ್ಯ ")
		elif ('FUT' in tag_verb):
			
			to_the_file.append("ಇದು ಭವಿಷ್ಯತ್‌ಕಾಲ ವಾಕ್ಯ")
		#print('N.SL' in tag_noun)
		if (('N.SL'in tag_noun and 'N.SL' in tag_verb) or ('N.PL'in tag_noun and 'N.PL' in tag_verb) or (('M.SL'in tag_noun or 'MFN.SL' in tag_noun) and ('M.SL' in tag_verb or 'MFN.SL' in tag_verb)) or 
	(('M.PL'in tag_noun or 'MFN.PL' in tag_noun)and ('M.PL' in tag_verb or 'MFN.PL' in tag_verb)) or 
	(('F.SL'in tag_noun or 'MFN.SL' in tag_noun) and ('F.SL' in tag_verb or 'MFN.SL' in tag_verb)) or 
	(('F.PL'in tag_noun or 'MFN.PL' in tag_noun)and ('F.PL' in tag_verb or 'MFN.PL' in tag_verb))):

			
			to_the_file.append("ಈ ವಾಕ್ಯದಲ್ಲಿ ಕಾಲ ಮತ್ತು ಲಿಂಗ ಸರಿಯಾಗಿದೆ!")
			if ( 'P1' in tag_noun and 'P1' in tag_verb):
				
				to_the_file.append("ಈ ವಾಕ್ಯ ಉತ್ತಮ ಪುರುಷದಲ್ಲಿದೆ ಮತ್ತು ಇದರ ಕತೃ ಕ್ರಿಯಾಪದಗಳು ಹೊಂದಿಕೊಂಡಿವೆ")
			elif ( 'P2' in tag_noun and 'P2' in tag_verb):
				
				to_the_file.append("ಈ ವಾಕ್ಯ ಮಧ್ಯಮ ಪುರುಷದಲ್ಲಿದೆ ಮತ್ತು ಇದರ ಕತೃ ಕ್ರಿಯಾಪದಗಳು ಹೊಂದಿಕೊಂಡಿವೆ")
			elif (( 'P3' in tag_noun and 'P3' in tag_verb) or ('P3' in tag_verb)):
				
				to_the_file.append("ಈ ವಾಕ್ಯ ಪ್ರಥಮ ಪುರುಷದಲ್ಲಿದೆ ಮತ್ತು ಇದರ ಕತೃ ಕ್ರಿಯಾಪದಗಳು ಹೊಂದಿಕೊಂಡಿವೆ")
			elif ('P1' in tag_noun and 'P3' in tag_verb):
				
				to_the_file.append("ಈ ವಾಕ್ಯ ಉತ್ತಮ ಪುರುಷದಲ್ಲಿದೆ ಮತ್ತು ಇದರ ಕತೃ ಕ್ರಿಯಾಪದಗಳು ಹೊಂದಿಕೊಂಡಿವೆt")
			elif ('P2' in tag_noun and 'P3' in tag_verb):
				
				to_the_file.append("ಈ ವಾಕ್ಯ ಮಧ್ಯಮ ಪುರುಷದಲ್ಲಿದೆ ಮತ್ತು ಇದರ ಕತೃ ಕ್ರಿಯಾಪದಗಳು ಹೊಂದಿಕೊಂಡಿವೆ")
			elif ('P1' in tag_verb or 'P2' in tag_verb):
				
				to_the_file.append("ವಾಕ್ಯದ ಪುರುಷ ಪ್ರಯೋಗದಲ್ಲಿ ತಪ್ಪಿದೆ ಮತ್ತು ಇದರ ಕತೃ ಕ್ರಿಯಾಪದಗಳು ಹೊಂದಿಕೊಂಡಿಲ್ಲ")
		elif found==0:
			
			to_the_file.append("ಈ ವಾಕ್ಯದ ಲಿಂಗ ಪ್ರಯೋಗದಲ್ಲಿ ತಪ್ಪಿದೆ.!!!!")
		elif found==1:
			
			to_the_file.append("ಈ ವಾಕ್ಯದಲ್ಲಿ ಕತೃ ಅಥವಾ ಕ್ರಿಯಾಪದ ಇಲ್ಲ. ದಯವಿಟ್ಟು ಪುನಃ ಪ್ರಯತ್ನಿಸಿರಿ")
		to_the_file.append("ಫಲಿತಾಂಶ  subject-verb_agreement.txt ಯಲ್ಲಿದೆ !")
		
		#to_the_file.append("------------------------------------------------------")
		ret_list.insert(1,to_the_file)
		output_file="subject-verb_agreement.txt"
		out_file=open(output_file,"a")
		for word in to_the_file:
			out_file.write("%s\n" % word)
		return ret_list
		
	else:
		
		
		list1=[]
		    
		diccy= open("hello_stripped.txt", "r")
		morphology= open("morphology1.txt", "r")
		to_the_file=[]	
		lines=diccy.readlines()
				
		d=0
		correct_input=""
		dictionaryWords=[]
		
		for line in morphology:
			dictionaryWords.append(line)

		#putting each word in list
		for a in range(0,305570):
			dictionaryWords.append(dictionaryWords[a].strip())

		completion_dawg = dawg.CompletionDAWG(dictionaryWords)
		#print(given_word)
		to_the_file.append(given_word)
		word = given_word.split()
		pronoun_value=""
		verb=0
		noun=0
		tag_verb=""
		tag_pronoun=""
		noun_value=""
		tag_noun=""
		pronoun=0
		found=0
		flag=0
		tag_verb=""
		for letter in word:
			suggest_word=[]
			suggest_line=[]
			ret_list=[]
			#print(letter)
			if letter not in completion_dawg:
				for inflection in dictionaryWords:
					d=distance(letter,inflection)
					if d<2:
						suggest_word.append(inflection)
				#print(suggest_word)
				if suggest_word:
					suggest_word=list(set(suggest_word))
					for suggestion in suggest_word:
						suggest_line.append(given_word.replace(letter,suggestion))
					ret_list.append(0)
					ret_list.insert(1,"The sentence has a spell error!")
					ret_list.insert(2, suggest_line)
					return ret_list
			nlines=0
			for line in lines:
				nlines += 1
			
				if(((letter+"\n")==line)==True):
		
					line_no=nlines
		
					if noun_value!="" and flag==0:
						tag_noun=lines[nlines]
											
						flag=1
						noun=1
					if flag==1 and (line[:-1].endswith(('iMda','u'))==True) and lines[nlines].startswith('N'):
						tag_noun=""
						noun_value=""
						flag=0
						noun=0
					if (lines[nlines].startswith('N') and noun==0 and (line[:-1].endswith(('iMda','u'))==True) and (line[:-1].endswith('annu')==False) and noun_value==""):
								
						#to_the_file.append("Noun is "+ letter)
										
						tag_noun=lines[nlines]
				
						noun=1
					elif ((lines[nlines].startswith('ITER') or lines[nlines].startswith('PROG') or lines[nlines].startswith('ABS'))):
						
						#to_the_file.append("Verb is " + lines[nlines-1])					
	
						tag_verb=lines[nlines]
						verb=1
					elif(lines[nlines].startswith('PRO') and pronoun==0):
								
						
						pronoun_value=lines[nlines-1]
						if pronoun_value[:-1]=="nanna":
							number=word.index(letter)+1
							noun_value=word[number]
							
							if noun_value not in dict_dawg:
								noun_value=""
							
						#to_the_file.append("Pronoun is " + lines[nlines-1])	
						
						tag_pronoun=lines[nlines]
						pronoun=1
											
				if (noun==1 and verb==1):
					break;
		nlines=line_no
		if ((tag_pronoun=="")==False) and (tag_noun==""):
			tag_noun=tag_pronoun
			noun=pronoun
		if verb==0 or noun==0:
			found=1
		ret_list.insert(0,1)	
	
		if ('PAST' in tag_verb):
			
			to_the_file.append("The sentence is in past tense")
		elif ('PRES' in tag_verb):
			
			to_the_file.append("The sentence is in present tense")
		elif ('FUT' in tag_verb):
			
			to_the_file.append("The sentence is in future tense")
		#print('N.SL' in tag_noun)
		if (('N.SL'in tag_noun and 'N.SL' in tag_verb) or ('N.PL'in tag_noun and 'N.PL' in tag_verb) or (('M.SL'in tag_noun or 'MFN.SL' in tag_noun) and ('M.SL' in tag_verb or 'MFN.SL' in tag_verb)) or 
	(('M.PL'in tag_noun or 'MFN.PL' in tag_noun)and ('M.PL' in tag_verb or 'MFN.PL' in tag_verb)) or 
	(('F.SL'in tag_noun or 'MFN.SL' in tag_noun) and ('F.SL' in tag_verb or 'MFN.SL' in tag_verb)) or 
	(('F.PL'in tag_noun or 'MFN.PL' in tag_noun)and ('F.PL' in tag_verb or 'MFN.PL' in tag_verb))):

			
			to_the_file.append("The Gender and the Tense match!")
			if ( 'P1' in tag_noun and 'P1' in tag_verb):
				
				to_the_file.append("The person is P1 and the sentence has subject-verb agreement")
			elif ( 'P2' in tag_noun and 'P2' in tag_verb):
				
				to_the_file.append("The person is P2 and the sentence has subject-verb agreement")
			elif (( 'P3' in tag_noun and 'P3' in tag_verb) or ('P3' in tag_verb)):
				
				to_the_file.append("The person is P3 and the sentence has subject-verb agreement")
			elif ('P1' in tag_noun and 'P3' in tag_verb):
				
				to_the_file.append("The person is P1 and the sentence has subject-verb agreement")
			elif ('P2' in tag_noun and 'P3' in tag_verb):
				
				to_the_file.append("The person is P2 and the sentence has subject-verb agreement")
			elif ('P1' in tag_verb or 'P2' in tag_verb):
				
				to_the_file.append("Wrong person relationship and the sentence has NO subject-verb agreement")
		elif found==0:
			print("Error!!Gender in subject and verb dont match!!\n")
			to_the_file.append("Error!!Gender in subject and verb dont match!!\n")
		elif found==1:
			
			to_the_file.append("Verb or Subject is missing in the sentence!! Please check again")
		to_the_file.append("The output file subject-verb_agreement.txt is generated!")
		
		to_the_file.append("------------------------------------------------------")
		ret_list.insert(1,to_the_file)
		output_file="subject-verb_agreement.txt"
		out_file=open(output_file,"a")
		for word in to_the_file:
			out_file.write("%s\n" % word)
		return ret_list

some_list=semantic("ರಾಮನು ಕಾಡಿಗೆ ಹೋದನು",3)
print(some_list[1])
#print(some_list[2])

