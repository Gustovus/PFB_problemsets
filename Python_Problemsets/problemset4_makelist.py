#!/usr/bin/env

dna = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

count = 0

for seq in dna:
	print(str(count)+'\t'+str(len(seq))+'\t'+seq+'\n')
	count += 1

tupleseq = [(seq, len(seq)) for seq in dna]

for tup in tupleseq:
	print(tup[1],'\t',tup[0],'\n')
