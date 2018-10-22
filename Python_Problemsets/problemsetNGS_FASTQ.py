#!/usr/bin/env python3

from Bio import SeqIO

fastqdict = {}
#fastqdict = SeqIO.to_dict(SeqIO.parse('four_reads.fastq', 'fastq'))
#print(fastqdict)
cut_qual = ''
cut_seq = ''
QualPlus = 0

for seq_record in SeqIO.parse('four_reads.fastq', 'fastq'):
#	fastqdict[seq_record.id] = seq_record.seq
#print(fastqdict)
	fastq = seq_record.format('fastq')
	cut_qual = seq_record.letter_annotations['phred_quality']
	cut_qual = cut_qual[5:]
	cut_seq = seq_record.seq
	cut_seq = cut_seq[5:]
#	seqName, seq, chaff, qual = fastq.split('\n', 3)

	for qual in seq_record.letter_annotations['phred_quality']:
		if qual > 30:
			QualPlus += 1
	print(QualPlus)
	QualPlus = 0

print(cut_qual)

