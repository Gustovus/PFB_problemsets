#!/usr/bin/env python3

import re

monst = open('bionet.py', 'r')


dictlist = []
count = 0

for line in monst:
	if not line.startswith('####'):
		print(line)	
print(count)

