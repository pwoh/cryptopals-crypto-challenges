import collections, sys, string

freq_dict = {}
files = ['corpus/11-0.txt', 'corpus/1342-0.txt', 'corpus/pg84.txt'] #top 3 project gutenburg

total = 0

for filename in files:
	with open(filename) as f:
		for l in f:
			for c in l:
				if c not in string.printable or c in "\t\n\r\x0b\x0c":
					continue
				if c not in freq_dict:
					freq_dict[c] = 0
				freq_dict[c] += 1
				total += 1

print freq_dict

for key, value in freq_dict.iteritems():
	freq_dict[key] = float(value)/float(total)
print freq_dict