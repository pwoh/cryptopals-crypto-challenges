def find_repeating(blockSize, ciphertext):
	blocks = [ciphertext[i:i+blockSize] for i in xrange(0, len(ciphertext), blockSize)]
	repeated = 0
	for i in xrange(0,len(blocks)):
		for j in xrange(i+1,len(blocks)):
			if blocks[i] == blocks[j]:
				repeated += 1
	return repeated

if __name__ == '__main__':
	bestLine = ''
	bestLineNum = 0
	mostRepeating = 0
	with open('8.txt') as f:
		for lineNum, line in enumerate(f, 1):
			if line != '\n':
				ciphertext = line.strip().decode('hex')
				repeating = find_repeating(16, ciphertext)
				if repeating > mostRepeating:
					bestLine = ciphertext
					mostRepeating = repeating
					bestLineNum = lineNum
	print bestLine
	print mostRepeating
	print bestLineNum