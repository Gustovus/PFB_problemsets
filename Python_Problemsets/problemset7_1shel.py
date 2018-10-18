#!/usr/bin/env python3

import re
readShel = open('Python_07_nobody.txt', 'r')

Shel = readShel.read()

for found in re.finditer(r"Nobody", Shel):
	print(found.group(0), (found.start(0)+1))

subShel = re.sub(r'Nobody', 'Eric', Shel)
print(subShel)

