#!/usr/bin/env python3

import sys

dna = sys.argv[1]

dna_nocase = dna.lower()

print("There are", dna_nocase.count('a'), "A's in this sequence")
print("There are", dna_nocase.count('t'), "T's in this sequence")
print("There are", dna_nocase.count('g'), "G's in this sequence")
print("There are", dna_nocase.count('c'), "C's in this sequence")
print("There are", len(dna_nocase), "nucleotides in this sequence")

print("The AT content is", (dna_nocase.count('a') + dna_nocase.count('t'))/ len(dna_nocase))
print("The GC content is", (dna_nocase.count('g') + dna_nocase.count('c'))/ len(dna_nocase))

subdna = dna[99:200]
print(subdna)
subdna_nocase = subdna.lower()
print("There are", subdna_nocase.count('g'), "G's in this substring")
