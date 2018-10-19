#!/usr/bin/env python3

import sys

dna_unr = sys.argv[1]
maxline_inp = sys.argv[2]

dna_inp = open(dna_unr, 'r')
dna_inp = dna_inp.read()

def DNAshort(dna, maxline):
	dna = dna.replace('\n', '')
	output = ''
	for i in range(0,len(dna),maxline):
		output += dna[i:i+maxline]+'\n'
	print(output)

def GCcontent(dna):
	countC = dna.count('C')
	countG = dna.count('G')
	GCcont = ((countG + countC)/len(dna))
	return GCcont

DNAshort(dna_inp, int(maxline_inp))
print(GCcontent(dna_inp))

