from Crypto.Cipher import AES
import base64

def aes_ecb_decrypt(ciphertext, key):
	decryptor = AES.new(key, AES.MODE_ECB)
	plaintext = decryptor.decrypt(ciphertext)
	return plaintext

if __name__ == '__main__':
	ciphertext = base64.b64decode(open('7.txt', 'r').read())
	print aes_decrypt(ciphertext, 'YELLOW SUBMARINE')