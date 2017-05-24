import base64 
from Crypto.Cipher import AES
from ch9_pkcs7_padding import pkcs7_padding
from ch11_ecbcbc_detection_oracle import random_bytes
from ch11_ecbcbc_detection_oracle import detect_block_cipher_mode

key = random_bytes(16)
suffix = '''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
blocksize = 16
encryptor = AES.new(key, AES.MODE_ECB)

def oracle_encrypt(plaintext):
    return encryptor.encrypt(pkcs7_padding(plaintext + base64.b64decode(suffix), blocksize))

def find_blocksize(blackbox):
    s = ''
    len0 = len(blackbox(s))
    while True:
        s += 'A'
        curlen = len(blackbox(s))
        if curlen != len0:
            return curlen - len0

def find_unknown_byte(blackbox, blocksize, knownprefix):
    bytenumber = len(knownprefix) + 1
    inputblock = '0'*(blocksize - bytenumber%blocksize)
    outputblock = blackbox(inputblock)
    guesslen = len(inputblock) + len(knownprefix) + 1
    outputdict = {}
    for i in xrange(0, 256): #extended ascii range
        guessoutput = blackbox(inputblock + knownprefix + chr(i))
        outputdict[guessoutput[0:guesslen]] = chr(i)
    return outputdict.get(outputblock[0:guesslen])

def find_unknown_string(blackbox):
    blocksize = find_blocksize(blackbox)
    if detect_block_cipher_mode(blackbox) != 'ECB':
        print 'Not ECB'
        return None

    knownprefix = ''
    while True:
        nextbyte = find_unknown_byte(blackbox, blocksize, knownprefix)
        if nextbyte:
            knownprefix += nextbyte
        else:
            return knownprefix

if __name__ == '__main__':
    print find_unknown_string(oracle_encrypt)