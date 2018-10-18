#!/usr/bin/env python3

import re

headcrack = open('Python_07.fasta', 'r')

headhunt = headcrack.read()

for found in re.finditer(r"\>(\S+)(.+\n)", headhunt):
	print("Gene id:", found.group(1), "Description:", found.group(2)) 
	
