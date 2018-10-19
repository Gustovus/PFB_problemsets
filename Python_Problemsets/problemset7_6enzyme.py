#!/usr/bin/env python3

import re

seq1 = open('Python_07_ApoI.fasta', 'r')

seq1readhead = seq1.read()

seq1read = re.sub(r'(.?\n)', r'', seq1readhead)

seq1read = seq1read.replace('\n', '')

for found in re.finditer(r"[GA]AATT[CT]", seq1read):
	print(found.start(0)+1)

cutseq = re.sub(r'([GA])(AATT[CT])', r'\1^\2', seq1read)


cutfrags = cutseq.split('^')

sortfrags = sorted(cutfrags, key=len)

sortfrags = sortfrags[::-1]
print(sortfrags)

