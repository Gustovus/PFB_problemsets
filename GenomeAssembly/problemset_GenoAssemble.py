#!/usr/bin/env python3

from Bio import SeqIO

assemble_open = open('ecoliPB-filtered_0.50.contigs.fasta', 'r')

fasta_dict = SeqIO.to_dict(SeqIO.parse(assemble_open, 'fasta'))
contiglen = []

print(len(fasta_dict))

for seq in fasta_dict:
	contiglen.append((len(fasta_dict[str(seq)].seq)))

contiglen = sorted(contiglen)
contiglen = contiglen[::-1]
print(contiglen)

mincontig = min(contiglen)
maxcontig = max(contiglen)
sumcontig = sum(contiglen)
halfcont = int(.5*(sumcontig))
L50count = 0
contigsum = 0

print(sumcontig, maxcontig, mincontig)

for contig in contiglen:
	if contigsum < halfcont:
		contigsum += contig
		L50count += 1

print('N50:', contiglen[L50count-1], 'L50:', L50count)
