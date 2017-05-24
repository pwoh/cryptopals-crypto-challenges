def pkcs7_padding(s, blocksize):
	c = blocksize - (len(s) % blocksize)
	return s + chr(c)*c

if __name__ == '__main__':
	s = "YELLOW SUBMARINE"
	ans = "YELLOW SUBMARINE\x04\x04\x04\x04"
	myAns = pkcs7_padding(s, 20)
	assert myAns == ans