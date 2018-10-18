#!/usr/bin/env python3

import re

seq1 = open('Python_07_ApoI.fasta', 'r')

seq1read = seq1.read()

for found in re.finditer(r"[GA]AATT[CT]", seq1read):
	print(found.start(0)+1)

cutseq = re.sub(r'([GA])(AATT[CT])', r'\1^\2', seq1read)
print(cutseq)

