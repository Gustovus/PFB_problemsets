#!/usr/bin/env python3

import re
import sys

multifasta = sys.argv[1]
#takes a multifasta input file

fasta = open(multifasta, 'r')
#opens the fasta input and reads it

seqs_dict = {}


for line in fasta:
	line = line.rstrip()
#removes extra line end
	if line.startswith('>'):
		find = re.search(r'>(\S+)', line)
		geneName = find.group(1)
		seqs_dict[geneName] = {'A':0, 'C':0, 'T':0, 'G':0}
	if not line.startswith('>'):
		for char in line:
			if char == 'T':
				seqs_dict[geneName]['T'] += 1
			elif char == 'G':
				seqs_dict[geneName]['G'] += 1
			elif char == 'C':
				seqs_dict[geneName]['C'] += 1
			elif char == 'A':
				seqs_dict[geneName]['A'] += 1
			#counts each line and tallies
print(seqs_dict)
			
