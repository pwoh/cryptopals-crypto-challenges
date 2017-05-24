from ch3_singlebyte_xor import bruteforce_singlexor, score_freq

def detect_singlechar_xor(lines):
    bestScore = 0
    bestDecoded = ''
    for line in lines:
        hexDecoded = line.strip().decode('hex')
        xorDecoded = bruteforce_singlexor(hexDecoded)
        if xorDecoded:
            score = score_freq(xorDecoded)
            if (score > bestScore):
                bestScore = score
                bestDecoded = xorDecoded
    return bestDecoded

if __name__ == '__main__':
    with open('4.txt') as f:
        lines = f.readlines()
        print detect_singlechar_xor(lines)