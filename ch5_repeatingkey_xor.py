def repeatingkey_xor(s, key):
    decoded = ''
    for i, c in enumerate(s):
        decoded = decoded + chr(ord(c)^ord(key[i%len(key)]))
    return decoded

def ascii_to_hex(s):
    return ''.join([c.encode('hex') for c in s])

if __name__ == '__main__':
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = 'ICE'
    encoded = ascii_to_hex(repeatingkey_xor(s,key))
    print encoded
    ans = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    assert encoded == ans

    print ascii_to_hex(repeatingkey_xor('The quick brown fox jumped over the lazy dog.', 'FROG'))
    print ascii_to_hex(repeatingkey_xor('The Moral Law causes the people to be in complete accord with their ruler, so that they will follow him regardless of their lives, undismayed by any danger. Heaven signifies night and day, cold and heat, times and seasons. Earth comprises distances, great and small; danger and security; open ground and narrow passes; the chances of life and death. The Commander stands for the virtues of wisdom, sincerity, benevolence, courage and strictness. By method and discipline are to be understood the marshaling of the army in its proper subdivisions, the graduations of rank among the officers, the maintenance of roads by which supplies may reach the army, and the control of military expenditure. These five heads should be familiar to every general: he who knows them will be victorious; he who knows them not will fail.', 'SUN'))