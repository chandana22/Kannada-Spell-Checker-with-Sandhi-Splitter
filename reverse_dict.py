#code to reverse the dictionary and write it in a file
# Author Akshatha dtd 13/03/15

dictWords=[]
r_dictWords=[]
f = open("dictionary_15k.txt", "r")

#read and append words to dictWords
for line in f:
	dictWords.append(line.strip())

for word in dictWords:
	w=word[::-1]
	r_dictWords.append(w)
	
write_f=open("reverse_dictionary_15k.txt","w")

for word in r_dictWords:
	write_f.write("%s\n" % word)
