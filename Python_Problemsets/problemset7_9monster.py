#!/usr/bin/env python3

import re

monst = open('bionet.py', 'r')


dictlist = {}

for line in monst:
	line = line.rstrip()
	if not line.startswith('####'):
		line = line.replace(' (', '_(')
		print(line)
		enzyme,cutsite = line.split()
		dictlist[enzyme] = cutsite

print(dictlist)

		
