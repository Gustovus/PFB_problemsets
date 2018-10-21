#!/usr/bin/env python3

from Bio import SeqIO

seq_dict = {} 

for seq_record in SeqIO.parse('human_cds.fasta', 'fasta'):
	seq_dict[seq_record.id] = seq_record.seq
	countG = (seq_record.seq).count('G')
	countC = (seq_record.seq).count('C')
	countT = (seq_record.seq).count('T')
	countA = (seq_record.seq).count('A')
	print(seq_record.id, '\t', ((countC+countG)/len(seq_record)))
