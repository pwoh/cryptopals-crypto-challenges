import base64

#I'm killing your brain like a poisonous mushroom

def hexToBase64(s):
    return base64.b64encode(s.decode('hex'))

myEncoded = hexToBase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
ans = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
assert thing == str(ans)
