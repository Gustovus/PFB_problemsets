#!/usr/bin/env python3

import sys

dna = sys.argv[1]
dna = dna.upper()

ecor1start = 'GAATTC'
dna_start = dna.find(ecor1start)

print(((dna_start)+1), "is the start site and", ((dna_start)+6), "is the end site")


