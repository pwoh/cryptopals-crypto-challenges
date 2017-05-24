from Crypto.Cipher import AES
from ch9_pkcs7_padding import pkcs7_padding
from ch11_ecbcbc_detection_oracle import random_bytes

def parse_encoded_kv(s):
    curkey = ''
    curval = None
    dic = {}
    for c in s:
        if c == '=':
            curval = ''
        elif c == '&':
            dic[curkey] = curval
            curkey = ''
            curval = None
        elif curval is None:
            curkey += c
        else:
            curval += c
    dic[curkey] = curval #last one
    return dic

def sanitise(s): 
    return s.replace('&', '').replace('=', '')

def encode_kv(tuplist):
    s = ''
    for (k, v) in tuplist:
        if s != '':
            s += '&'
        s += str(k) + '=' + str(v)
    return s

def profile_for(email):
    email = sanitise(email)
    items = [
        ('email', email),
        ('uid', 10),
        ('role', 'user')
    ]
    return encode_kv(items)

key = random_bytes(16) #fixed key
aes_ecb = AES.new(key, AES.MODE_ECB)
blocksize = 16

def encrypt_profile_for(email):
    profile = profile_for(email)
    profile = pkcs7_padding(profile, blocksize)
    return aes_ecb.encrypt(profile)

def pkcs7_unpadding(s):
    padlen = ord(s[-1])
    return s[0:-padlen]

def pkcs7_padding(s, blocksize):
    c = blocksize - (len(s) % blocksize)
    return s + chr(c)*c

def decrypt_profile_for(ciphertext):
    plaintext = aes_ecb.decrypt(ciphertext)
    plaintext = pkcs7_unpadding(plaintext)
    return parse_encoded_kv(plaintext)

def get_encrypted_adminprofile():
    ciphertext1 = encrypt_profile_for('legit@abc.com')
    ciphertext2 = encrypt_profile_for('hacker@xy.admin' + chr(11)*11)
    return ciphertext1[0:32] + ciphertext2[16:32]

if __name__ == '__main__':
    assert parse_encoded_kv('foo=bar&baz=qux&zap=zazzle') == {'foo': 'bar',  'baz': 'qux',  'zap': 'zazzle'}
    assert profile_for('foo@bar.com') == 'email=foo@bar.com&uid=10&role=user'
    assert decrypt_profile_for(encrypt_profile_for('abc@def.com')) == {'email': 'abc@def.com', 'uid': '10', 'role': 'user'}

    c = get_encrypted_adminprofile()
    print decrypt_profile_for(c)