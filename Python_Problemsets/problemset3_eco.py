#!/usr/bin/env python3

import sys

dna = sys.argv[1]
dna = dna.upper()

ecor1start = 'GAATTC'
dna_start = dna.find(ecor1start)

dnastring = "{} is the start site and {} is the end site"
print(dnastring.format(dna_start+1, dna_start+6))

print(((dna_start)+1), "is the start site and", ((dna_start)+6), "is the end site")
print(dna[(dna_start):(dna_start+6)])

