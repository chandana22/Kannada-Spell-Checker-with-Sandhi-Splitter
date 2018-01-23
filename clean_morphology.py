file_open=open("morph_out.txt","r")
morph_words=[]
for line in file_open:
	line=line.strip()
	if line.endswith(':'):
		continue
	morph_words.append(line)
	
file_out=open("morph_forms.txt","w")
for word in morph_words:
	file_out.write("%s\n" % word)
