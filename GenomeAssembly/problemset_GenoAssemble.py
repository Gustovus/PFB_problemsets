#!/usr/bin/env python3

from Bio import SeqIO

assemble_open = open('ecoliPB-filtered_0.50.contigs.fasta', 'r')

fasta_dict = SeqIO.to_dict(SeqIO.parse(assemble_open, 'fasta'))
contiglen = []

print(len(fasta_dict))

for seq in fasta_dict:
	contiglen.append((len(fasta_dict[str(seq)].seq)))

contiglen = sorted(contiglen)
print(contiglen)

maxcontig = contiglen[len(contiglen)-1]
mincontig = contiglen[0]

print(maxcontig, mincontig)

