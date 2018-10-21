#!/usr/bin/env python3

from Bio import SeqIO

for seq_record in SeqIO.parse('Python_08.fasta', 'fasta'):
	print('ID', seq_record.id)
	print('Sequence', seq_record.seq)
	print('Length', len(seq_record))
	countG = (seq_record.seq).count('G')
	countC = (seq_record.seq).count('C')
	countT = (seq_record.seq).count('T')
	countA = (seq_record.seq).count('A')
	

