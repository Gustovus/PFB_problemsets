#!/usr/bin/env python3

import sys
import re

bam_inp = open(sys.argv[1], 'r')
bam_dict = {}
bam_count = {}

for line in bam_inp:
	line = line.strip()
	line = line.split('\t')
	read = line[0]
	transplit = line[2]
	transcr = transplit.split('^') 
	transcr = transcr[0]
	if transcr not in bam_dict.keys():
		bam_dict[transcr] = {read}
	if transcr in bam_dict.keys():
		bam_dict[transcr].add(read)

bamsort = sorted(bam_dict, key = lambda x: len(bam_dict[x]), reverse = True)

for line in bamsort:
	print(line, '\t', len(bam_dict[line]))
