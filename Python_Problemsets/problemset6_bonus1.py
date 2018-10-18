#!/usr/bin/env python3

file_seq = open("Python_06.seq1.txt", "r")

countA = 0
countT = 0
countG = 0
countC = 0

nucCount = {"A" :str(countA), "T" : countT, "G" : countG, "C" : countC}

print(nucCount['A'])

for line in file_seq:
	line = line.rstrip()
	seqname, seq = line.split('\t')
	print(seq)
	print(seq.count('A'))
	countA += seq.count('A')
	print(countA)
	countT = seq.count('T')
	countC = seq.count('C')
	countG = seq.count('G')
	print(nucCount)
file_seq.close()
print(nucCount)
