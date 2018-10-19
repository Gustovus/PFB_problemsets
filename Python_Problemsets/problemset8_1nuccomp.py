#!/usr/bin/env python3

import re
import sys

multifasta = sys.argv[1]
#takes a multifasta input file

fasta = open(multifasta, 'r')
#opens the fasta input and reads it

seqs = {}
count = 0

for line in fasta:
	line = line.rstrip()
#removes extra line end
	if line.startswith('>'):
		find = re.search(r'>(\S+)', line)
		header = find.group(1)
		seqs[header] = ''
	if not line.startswith('>'):
		seqs[header] += line

#skips over the header
#		''.join(line)
		countT = 0
		countG = 0
		countC = 0
		countA = 0
		for char in line:
			if char == 'T':
				countT += 1
			elif char == 'G':
				countG += 1
			elif char == 'C':
				countC += 1
			elif char == 'A':
				countA += 1
			#counts each line and tallies
		seqs.append({})
		print(seqs)
		seqs[count][header]=(countT, countG, countC, countA)
		count += 1
			
