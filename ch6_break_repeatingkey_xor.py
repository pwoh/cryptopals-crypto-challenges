import base64 
import sys
from ch3_singlebyte_xor import bruteforce_singlexor
from ch5_repeatingkey_xor import repeatingkey_xor
import itertools

def hammingDist(s1, s2):
	return binaryDiff(bytearray(s1),bytearray(s2))

def binaryDiff(b1, b2):
	diff = 0
	for c1,c2 in zip(b1,b2):
		diff += bin(c1^c2).count('1')
	return diff

def normalisedEditDist(decodedBytes, keySize):
	first = decodedBytes[0:keySize]
	second = decodedBytes[keySize:keySize*2]
	third = decodedBytes[keySize*2:keySize*3]
	fourth = decodedBytes[keySize*3:keySize*4]
	totalEditDist = hammingDist(first,second) + hammingDist(first,third) + hammingDist(first,fourth) + hammingDist(second,third) + hammingDist(second,fourth) + hammingDist(third,fourth)
	totalEditDist = totalEditDist/(float(keySize)*6)
	return totalEditDist

def findKeySize(decodedBytes):
	bestDist = sys.maxint
	bestKey = 0
	for k in range(2,41):
		dist = normalisedEditDist(decodedBytes, k)
		if (dist < bestDist):
			bestDist = dist
			bestKey = k
	return bestKey

def transposeBlocks(decodedBytes, keySize):
	blocks = [decodedBytes[i:i+keySize] for i in range(0, len(decodedBytes), keySize)]
	blocksTransposed = list(itertools.izip_longest(*blocks, fillvalue='\x00'))
	return [''.join(str(c) for c in block) for block in blocksTransposed]

def singleXorBlocks(decodedBytes, keySize):
	blocks = transposeBlocks(decodedBytes, keySize)
	return [bruteforce_singlexor(block)[0] for block in blocks]

if __name__ == '__main__':
	print hammingDist('this is a test','wokka wokka!!!')
	decodedBytes = base64.b64decode(open('6.txt', 'r').read())

	k = findKeySize(decodedBytes)
	finalKeyArray = singleXorBlocks(decodedBytes, k)
	finalKey = ''.join(chr(i) for i in finalKeyArray)
	print "finalKey=" + finalKey
	print repeatingkey_xor(decodedBytes, finalKey)
