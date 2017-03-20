def fixedXorHex(buf1, buf2):
    return '{:x}'.format((int(buf1,16)^int(buf2,16)))

buf1 = '1c0111001f010100061a024b53535009181c'
buf2 = '686974207468652062756c6c277320657965'
ans = '746865206b696420646f6e277420706c6179'
assert fixedXorHex(buf1,buf2) == ans