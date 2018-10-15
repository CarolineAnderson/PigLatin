def speakPigLatin(txt):
	txtArr = txt.split()
	vowels = ['a','e','i','o','u','y']
	newtxt = ''

	for word in txtArr:
		index  = 0
		
		while word[index] not in vowels:
			index+=1
		if index ==0:
			extra = 'yay'
		else:
			extra = 'ay'
		word = word[index:]+word[0:index] +extra+ ' '
		newtxt += word

	return newtxt
	

