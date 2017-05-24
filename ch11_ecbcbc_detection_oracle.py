from Crypto import Random
from Crypto.Random import random
from Crypto.Cipher import AES
from ch10_cbc_mode import cbc_encrypt
from ch9_pkcs7_padding import pkcs7_padding

def random_bytes(numBytes):
    rndfile = Random.new()
    return rndfile.read(numBytes)

def encrypt_ecbcbc(plaintext):
    blocksize = 16
    key = random_bytes(16)
    encryptor = AES.new(key, AES.MODE_ECB)

    plaintext = random_bytes(random.randint(5,10)) + plaintext + random_bytes(random.randint(5,10))
    plaintext = pkcs7_padding(plaintext, blocksize)
    if random.randint(0,1) == 0:
        print 'encrypting with ecb'
        return encryptor.encrypt(plaintext)
    else:
        print 'encrypting with cbc'
        return cbc_encrypt(encryptor, plaintext, blocksize, random_bytes(blocksize))

def detect_block_cipher_mode(blackbox):
    plaintext = '0'*48 #3 blocks of 0s
    ciphertext = blackbox(plaintext)
    if ciphertext[16:32] == ciphertext[32:48]: #check the 2nd and 3rd blocks
        return 'ECB'
    else:
        return 'CBC'

if __name__ == '__main__':
    print detect_block_cipher_mode(encrypt_ecbcbc)