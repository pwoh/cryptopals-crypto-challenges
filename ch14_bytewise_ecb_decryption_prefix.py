import base64 
from Crypto.Cipher import AES
from Crypto.Random import random
import itertools
from ch9_pkcs7_padding import pkcs7_padding
from ch11_ecbcbc_detection_oracle import random_bytes
from ch11_ecbcbc_detection_oracle import detect_block_cipher_mode
from ch12_bytewise_ecb_decryption import find_blocksize

key = random_bytes(16)
suffix = '''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
block_size = 16
rand_prefix_size = random.randint(1,100)
rand_prefix = random_bytes(rand_prefix_size)
encryptor = AES.new(key, AES.MODE_ECB)

def oracle_encrypt(plaintext):
    return encryptor.encrypt(pkcs7_padding(rand_prefix + plaintext + base64.b64decode(suffix), block_size))

def find_prefix_blocks(blackbox, blocksize):
    encryptEmpty = blackbox('')
    encryptBlock = blackbox('0'*blocksize)
    for i, (a,b) in enumerate(itertools.izip(encryptEmpty, encryptBlock)):
        if a != b:
            return i/blocksize

def find_prefix_remainder(blackbox, blocksize, numprefixblocks):
    k = (numprefixblocks+1)*blocksize
    for i in xrange(blocksize):
        encrypted = blackbox('0'*(2*blocksize + i))
        if encrypted[k:k+blocksize] == encrypted[k+blocksize:k+blocksize*2]:
            return i

def find_unknown_byte(blackbox, blocksize, knownprefix, fullprefixblocks, prefixremainder):
    bytenumber = len(knownprefix) + 1
    prefixfill = 'x'*prefixremainder
    inputblock = '0'*(blocksize - bytenumber%blocksize)
    outputblock = blackbox(prefixfill + inputblock)[(fullprefixblocks+1)*blocksize:]
    guesslen = len(inputblock) + len(knownprefix) + 1
    outputdict = {}
    for i in xrange(0, 256): #extended ascii range
        guessoutput = blackbox(prefixfill + inputblock + knownprefix + chr(i))[(fullprefixblocks+1)*blocksize:]
        outputdict[guessoutput[0:guesslen]] = chr(i)
    return outputdict.get(outputblock[0:guesslen])

def find_unknown_string(blackbox):
    blocksize = find_blocksize(blackbox)

    fullprefixblocks = find_prefix_blocks(blackbox, blocksize)
    prefixremainder = find_prefix_remainder(blackbox, blocksize, fullprefixblocks)

    knownprefix = ''
    while True:
        nextbyte = find_unknown_byte(blackbox, blocksize, knownprefix, fullprefixblocks, prefixremainder)
        if nextbyte:
            knownprefix += nextbyte
        else:
            return knownprefix

if __name__ == '__main__':
    print find_unknown_string(oracle_encrypt)