#!/usr/bin/env

dna = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

count = 0

for seq in dna:
	print(str(count)+'\t'+str(len(seq))+'\t'+seq+'\n')
	count += 1

