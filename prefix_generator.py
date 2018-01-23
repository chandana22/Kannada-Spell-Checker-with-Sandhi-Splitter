import init_sandhi_mod
from init_sandhi_mod import *

prefix_removed=[]

prefix_map={}
for word in dictWords:
	for lopa in lopa_places:
		if word.endswith(lopa):
			prefix_removed.append(word[:-1])
			key=word[:-1]
			prefix_map.setdefault(key,[])
			#prefix_removed.append("added this for pefix removed : "+word+" ==> "+word[:-1])
			prefix_map[word[:-1]].append(word[-1])
			
prefix_file=open("prefix_dictionary.py","w")
to_write=""
prefix_removed1=list(set(prefix_removed))
to_write="prefix_removed=['"
for word in prefix_removed1:
	to_write+=word+"','"
to_write=to_write[:-2]+"]\nprefix_map={}\n"	

for word in prefix_removed1:
	to_write+= "prefix_map['"+word+"']=['"
	for w in prefix_map[word]:
		to_write+=w+"','"
	to_write=to_write[:-2]
	to_write+="]\n"
	
	#+prefix_map[word]+"\n"
prefix_file.write(to_write)

print("prefix_dictionary.py generated") 		
