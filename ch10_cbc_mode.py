from Crypto.Cipher import AES
import base64

def cbc_encrypt(aes_ecb, plaintext, blocksize, init_vec):
	blocks = splitBlocks(plaintext, blocksize)
	ciphertext = ''
	prevBlock = init_vec
	for block in blocks:
		cipherblock = aes_ecb.encrypt(xor(block, prevBlock))
		ciphertext += cipherblock
		prevBlock = cipherblock
	return ciphertext

def cbc_decrypt(aes_ecb, ciphertext, blocksize, init_vec):
	blocks = splitBlocks(ciphertext, blocksize)
	plaintext = ''
	prevBlock = init_vec
	for block in blocks:
		plainblock = xor(aes_ecb.decrypt(block), prevBlock)
		plaintext += plainblock
		prevBlock = block
	return plaintext

def splitBlocks(s, blocksize):
	return [s[i:i+blocksize] for i in xrange(0, len(s), blocksize)]

def xor(s1,s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

if __name__ == '__main__':
	blocksize = 16
	aes_ecb = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
	init_vec = chr(0)*blocksize

	ciphertext = base64.b64decode(open('10.txt', 'r').read())
	plaintext = cbc_decrypt(aes_ecb, ciphertext, blocksize, init_vec)
	reciphertext = cbc_encrypt(aes_ecb, plaintext, blocksize, init_vec)

	print plaintext

	assert ciphertext == reciphertext