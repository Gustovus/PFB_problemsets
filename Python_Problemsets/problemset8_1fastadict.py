#!/usr/bin/env python3

import re
import sys

multifasta = sys.argv[1]
#takes a multifasta input file

fasta = open(multifasta, 'r')
#opens the fasta input and reads it

seq_dict = {}
seqs_dictcount = {}

for line in fasta:
	line = line.rstrip()
	if line.startswith('>'):
		find = re.search(r'>(\S+)', line)
		geneName = find.group(1)
		seq_dict[geneName] = ''
		seqs_dictcount[geneName] = {'A':0, 'C':0, 'T':0, 'G':0}
	if not line.startswith('>'):
		seq_dict[geneName] += line
		for char in line:
			if char == 'T':
				seqs_dictcount[geneName]['T'] += 1
			elif char == 'G':
				seqs_dictcount[geneName]['G'] += 1
			elif char == 'C':
				seqs_dictcount[geneName]['C'] += 1
			elif char == 'A':
				seqs_dictcount[geneName]['A'] += 1
		
#print(seq_dict)

#print(seqs_dictcount)

#for  in range(0, len(seq_dict[geneName])):
#	print(seq_dict[geneName][i:i+3])
#	if frame < 4:
#	print(seq_dict[geneName][0:3]) 
#			frame += 1
	
for geneName in seq_dict:
	print(seq_dict[geneName][0:3], seq_dict[geneName][3:6], seq_dict[geneName][6:9], seq_dict[geneName][9:12])

		
