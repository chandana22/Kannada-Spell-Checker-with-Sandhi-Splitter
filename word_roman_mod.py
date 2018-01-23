	
#creating a dictionary to store the mapping
roman_kaagunita={u'\u0CBE': 'aa',u'\u0CC1': 'u',u'\u0CCD': '',u'\u0CBF': 'i',u'\u0CC0' : 'ii',u'\u0CC2': 'uu', u'\u0CC3': 'R', u'\u0CC6': 'e', u'\u0CC7': 'ee',u'\u0CC8': 'ai',u'\u0CCA': 'o',u'\u0CCB': 'oo',u'\u0CCC': 'au',u'\u0CEF': 'r'}

#the words themselves to roman
roman={ u'\u0C85': 'a',u'\u0C86': 'aa',u'\u0C87': 'i',u'\u0C88': 'ii', u'\u0C89': 'u',u'\u0C8A': 'uu',u'\u0C8B': 'R',u'\u0C8E': 'e',u'\u0C8F': 'ee', u'\u0C90': 'ai',u'\u0C92': 'o', u'\u0C93': 'oo',u'\u0C94': 'au',u'\u0C82': 'M',u'\u0C83': 'H',u'\u0C95': 'ka',u'\u0C96': 'kha',u'\u0C97': 'ga',u'\u0C98': 'gha',u'\u0C99': 'nGa',u'\u0C9A': 'ca',u'\u0C9B': 'cha',u'\u0C9C': 'ja',u'\u0C9D': 'jha',u'\u0C9E': 'nYa',u'\u0C9F': 'Ta',u'\u0CA0': 'Tha',u'\u0CA1': 'Da',u'\u0CA2': 'Dha',u'\u0CA3': 'Na',u'\u0CA4': 'ta',u'\u0CA5': 'tha',u'\u0CA6': 'da',u'\u0CA7': 'dha',u'\u0CA8': 'na',u'\u0CAA': 'pa',u'\u0CAB': 'pha',u'\u0CAC': 'ba',u'\u0CAD': 'bha',u'\u0CAE': 'ma',u'\u0CAF': 'ya',u'\u0CB0': 'ra',u'\u0CB2': 'la',u'\u0CB5': 'va',u'\u0CB6': 'sha',u'\u0CB7': 'Sha',u'\u0CB8': 'sa',u'\u0CB9': 'ha',u'\u0CBE': '$', u'\u0CB3':'La',u'\u0CC1': '$',u'\u0CCD': '$',u'\u0CBF': '$',u'\u0CC0' : '$',u'\u0CC2': '$', u'\u0CC3': '$', u'\u0CC6': '$', u'\u0CC7': '$',u'\u0CC8': '$',u'\u0CCA': '$',u'\u0CCB': '$',u'\u0CCC': '$',u'\u0CEF': '$'}

#creating a dictionary to store the mapping in unicode
uni_kaagunita={'aa' : u'\u0CBE', 'u' : u'\u0CC1', 'i' : u'\u0CBF', 'ii' : u'\u0CC0', 'uu' : u'\u0CC2', 'R' : u'\u0CC3', 'e' : u'\u0CC6', 'ee' : u'\u0CC7', 'ai' : u'\u0CC8', 'o' : u'\u0CCA', 'oo' : u'\u0CCB', 'au' : u'\u0CCC'}

doubt={ 'r' : u'\u0CEF' }

#the words themselves to unicode
uni_vowel={ 'a' : u'\u0C85', 'aa' : u'\u0C86', 'i' : u'\u0C87', 'ii' : u'\u0C88','u': u'\u0C89', 'uu' : u'\u0C8A', 'R' : u'\u0C8B', 'e' : u'\u0C8E', 'ee' : u'\u0C8F', 'ai' : u'\u0C90', 'o' : u'\u0C92','oo' : u'\u0C93', 'au' : u'\u0C94'}
uni_visarga={'M' : u'\u0C82', 'H' : u'\u0C83'}
uni_conso={ 'ka' : u'\u0C95', 'kha' : u'\u0C96', 'ga' : u'\u0C97', 'gha' : u'\u0C98', 'nGa' : u'\u0C99', 'ca' : u'\u0C9A', 'cha' : u'\u0C9B', 'ja' : u'\u0C9C', 'jha' : u'\u0C9D', 'nYa' : u'\u0C9E' , 'Ta' : u'\u0C9F', 'Tha' : u'\u0CA0', 'Da' : u'\u0CA1', 'Dha' : u'\u0CA2', 'Na' : u'\u0CA3', 'ta' : u'\u0CA4', 'tha' : u'\u0CA5', 'da' : u'\u0CA6', 'dha' : u'\u0CA7', 'na' : u'\u0CA8' , 'pa' : u'\u0CAA', 'pha' : u'\u0CAB', 'ba' : u'\u0CAC', 'bha' : u'\u0CAD', 'ma' : u'\u0CAE', 'ya' : u'\u0CAF' , 'ra' : u'\u0CB0', 'la' : u'\u0CB2', 'va' : u'\u0CB5', 'sha' : u'\u0CB6', 'Sha' : u'\u0CB7', 'sa' : u'\u0CB8', 'ha' : u'\u0CB9', 'La' : u'\u0CB3' } 

#'$' : u'\u0CBE', '$' : u'\u0CC1' , '$' : u'\u0CCD', '$': u'\u0CBF', '$':u'\u0CC0', '$' : u'\u0CC2', '$': u'\u0CC3', '$': u'\u0CC6', '$': u'\u0CC7', '$':u'\u0CC8', '$': u'\u0CCA', '$':u'\u0CCB', '$':u'\u0CCC', '$':u'\u0CEF'}

def to_roman(word):
	r=""
	for c in word:
		#print(c)
		if c not in roman:
			c=""
			continue
		if roman[c]=='$':
			u2=r[0:-1]
			r=u2
			r+=roman_kaagunita[c]
		else:	
			r+=roman[c]
		prev=c
	return(r)


def to_uni(word):
	word_len=len(word)
	i=0
	r=""
	prev=1
	count=0
	while i<word_len:
		
		prev=i
		
		c=word[i]
		if c==" ":
			i=i+1
		c1=""
		c2=""
		c3=""
		
		if i<word_len-3:
			c3=word[i+3]
		if i<word_len-2:
			c2=word[i+2]
		if i<word_len-1:
			c1=word[i+1]
		
		#first two letters are vowels ex au ai
		if i<2 and c+c1 in uni_vowel:
			r=r+uni_vowel[c+c1]
			i=i+2
			continue
			
		#first letter is a swara ex a	
		if i==0 and c in uni_vowel:
			r=r+uni_vowel[c]
			i=i+1
			continue
			
		#anuswaara visarga
		if c=='M' or c=='H':
			r=r+uni_visarga[c]
			i=i+1
			continue
		
		if c+c1+'a' in uni_conso:
			c=c+c1
			c1=c2
			c2=c3
			i=i+1
			
		if c+'a' in uni_conso:
			r=r+uni_conso[c+'a']
			if c1 in uni_kaagunita or c1+c2 in uni_kaagunita:	
				if c1+c2 in uni_kaagunita: 
					r=r+uni_kaagunita[c1+c2]
					i=i+3
			
				elif c1 in uni_kaagunita:
					r=r+uni_kaagunita[c1]
					i=i+2
					
			elif c1+'a' in uni_conso or c1+c2+'a' in uni_conso or i==word_len-1 or c1=="":
				r=r+u'\u0CCD'
				i=i+1
			else:
				i=i+2
				

	return r
