#!/usr/bin/env python3

import sys

dna = sys.argv[1]
dna_sub = dna.upper()

dna_comp = dna_sub.replace("A", "t")
dna_comp = dna_comp.replace("T", "a")
dna_comp = dna_comp.replace("G", "c")
dna_comp = dna_comp.replace("C", "g")

dna_comp = dna_comp.upper()

print("5'", dna_comp[::-1], "3'")

