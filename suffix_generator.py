import init_sandhi_mod
from init_sandhi_mod import *

suffix_removed=[]

suffix_map={}
for word in dictWords:
	f=0
	for suffix in suffix_vowels1:
		if word.startswith(suffix):
			suffix_removed.append(word[2:])
			key=word[2:]
			suffix_map.setdefault(key,[])
			#prefix_removed.append("added this for pefix removed : "+word+" ==> "+word[:-1])
			suffix_map[word[2:]].append(suffix)
			print(word[2:])
			f=1
	for suffix in suffix_vowels2:
		if word.startswith(suffix) and f==0:
			suffix_removed.append(word[1:])
			key=word[1:]
			suffix_map.setdefault(key,[])
			#prefix_removed.append("added this for pefix removed : "+word+" ==> "+word[:-1])
			suffix_map[word[1:]].append(suffix)
			print(word[1:])
suffix_file=open("suffix_dictionary.py","w")

to_write=""
suffix_removed1=list(set(suffix_removed))
to_write="suffix_removed=['"
for word in suffix_removed1:
	to_write+=word+"','"
to_write=to_write[:-2]+"]\nsuffix_map={}\n"	

for word in suffix_removed1:
	to_write+= "suffix_map['"+word+"']=['"
	for w in suffix_map[word]:
		to_write+=w+"','"
	to_write=to_write[:-2]
	to_write+="]\n"
	
	#+prefix_map[word]+"\n"
suffix_file.write(to_write)

print("suffix_dictionary.py generated") 		
