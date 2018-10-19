#!/usr/bin/env python3

import sys
dna_unr = sys.argv[1]

dna_inp = open(dna_unr, 'r')
dna_inp = dna_inp.read()

def revcount(dna):
	dna_sub = dna.upper()
	dna_comp = dna_sub.replace("A", "t")
	dna_comp = dna_comp.replace("T", "a")
	dna_comp = dna_comp.replace("G", "c")
	dna_comp = dna_comp.replace("C", "g")
	dna_comp = dna_comp.upper()
	return dna_comp

print(revcount(dna_inp))

