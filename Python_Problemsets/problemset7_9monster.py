#!/usr/bin/env python3

import re
import sys

#enzymeinput = sys.argv[1]
#fastafile = sys.argv[2]

monst = open('bionet.py', 'r')
#fasta = open(fastafile, 'r')

dictlist = {}

for line in monst:
	line = line.rstrip()
	if not line.startswith('####'):
		line = line.replace(' (', '_(')
		enzyme,cutsite = line.split()
		if not enzyme in dictlist:
			dictlist[enzyme] = cutsite
		else:
			dictlist[enzyme].append(cutsite)
print(dictlist)

#for line in fasta:
#	if enzymeinput in dictlist:
#		if dictlist[enzymeinput] in line:
#			print(line)		
