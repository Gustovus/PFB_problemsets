#!/usr/bin/env python3

import sys
from Bio import SeqIO

fastq_inp = sys.argv[1]
kmerlen = sys.argv[2]
num_topkmer = sys.argv[3]

kmer = ''
kmerlen = int(kmerlen)
fastq_seq = '' 
kmercount = {}
num_topkmer = int(num_topkmer)

fastq = open(fastq_inp, 'r')

for seq_record in SeqIO.parse(fastq, "fastq"):
#parse through the fastq
	fastq_seq = str(seq_record.seq) 
#put all of the fastq into a large string
	for i in range(0, len(fastq_seq)):
#look at the entire length of the string
		key = fastq_seq[i:i+kmerlen]
#set the key of the dictionary to any sequence of the desired kmerlength
		if len(key) == kmerlen:
#this statement makes the count only apply to seq strings as long as the kmer
			if key not in kmercount:
				kmercount[key] = 1
#this searches for the presence of the seq string and if not found yet, sets it to 1 (needs the not before the 'in' instead of after the 'if'
			else:
				kmercount[key] += 1 
#if the seq is already present, increment its count by 1

kmercountsort = sorted(kmercount.keys(), key=lambda x: kmercount[x], reverse = True)

count = 0
for kmer in kmercountsort:
	if count < num_topkmer:
		print(kmer, '\t', kmercount[kmer])
		count += 1


