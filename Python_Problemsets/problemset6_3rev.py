#!/usr/bin/env python3

file_seq = open("Python_06.seq.txt", "r")

seq_place = {}

for line in file_seq:
	line = line.rstrip()
	seqname, seq = line.split('\t')
	seq_place[seqname] = seq	

for seqname in seq_place:
	dna_rev = seq.replace("A", "t")
	dna_rev = dna_rev.replace("T", "a")
	dna_rev = dna_rev.replace("G", "c")
	dna_rev = dna_rev.replace("C", "g")
	dna_rev = dna_rev.upper()
	print('>',seqname, ' This is the reverse complement', '\t', dna_rev[::-1], '\n')

file_seq.close()

