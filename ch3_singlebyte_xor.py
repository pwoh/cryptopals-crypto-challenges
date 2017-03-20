import string

#Cooking MC's like a pound of bacon

eng_freq={
'a':8.167,
'b':1.492,
'c':2.782,
'd':4.253,
'e':12.702,
'f':2.228,
'g':2.015,
'h':6.094,
'i':6.966,
'j':0.153,
'k':0.772,
'l':4.025,
'm':2.406,
'n':6.749,
'o':7.507,
'p':1.929,
'q':0.095,
'r':5.987,
's':6.327,
't':9.056,
'u':2.758,
'v':0.978,
'w':2.360,
'x':0.150,
'y':1.974,
'z':0.074}
#TODO punctuation

def score_freq(s):
	score = 0
	for c in s:
		if c in string.printable and c not in "\t\n\r\x0b\x0c":
			if c.lower() in eng_freq: #todo printable char
				score = score + eng_freq[c.lower()]
		else:
			return 0
	return score

def bruteforce_singlexor(s):
	bestScore = 0
	bestDecoded = ''
	bestKey = 0
	for i in range(0,256): #extended ascii range
	    decoded = ''.join(chr(ord(c)^i) for c in hexDecoded)
	    score = score_freq(decoded)
	    if (score > bestScore):
	        bestScore = score
	        bestDecoded = decoded
	        bestKey = i
	print bestDecoded, bestKey, bestScore

	return bestDecoded

hexEncoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
hexDecoded  = hexEncoded.decode('hex')
bruteforce_singlexor(hexDecoded)