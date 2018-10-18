#!/usr/bin/env

alp_genes = open("alpaca_all_genes.tsv", 'r')
stem_genes = open("alpaca_stemcellproliferation_genes.tsv", 'r')
pig_genes = open("alpaca_pigmentation_genes.tsv", 'r')
trans_genes = open("alpaca_transcriptionFactors.tsv", 'r')

all_lit = []
stem_lit = []
pig_lit = []
trans_lit = []

for line in alp_genes:
	line = line.rstrip()
	all_lit.append(line)

all_lit.pop(0)

for line in stem_genes:
	line = line.rstrip()
	stem_lit.append(line)

stem_lit.pop(0)

for line in pig_genes:
	line = line.rstrip()
	pig_lit.append(line)

pig_lit.pop(0)

for line in trans_genes:
	line = line.rstrip()
	trans_lit.append(line)

trans_lit.pop(0)

allset = set(all_lit)
stemset = set(stem_lit)
pigset = set(pig_lit)
transet = set(trans_lit)
print("These are not cell proliferation genes", allset - stemset)
print("These are both cell proliferation genes and pigmentation genes", stemset & pigset)
print("These are transcription factors for cell proliferation", transet & stemset)


