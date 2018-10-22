#!/usr/bin/env python3

import sys

def match(seq1, seq2, match, mismatch):
	seq_score = 0
	seq12r_score = 0
	seq1r2_score = 0
	rc2_score = 0
	seq1_lst = []
	seq2_lst = []
	seq1_revc = []
	seq2_revc = []
	for char in seq1:
		seq1_lst.append(char)
	for char in seq2:
		seq2_lst.append(char)
	seq1_revc = seq1.upper()
	seq1_revc = seq1_revc.replace('G', 'c')
	seq1_revc = seq1_revc.replace('C', 'g')
	seq1_revc = seq1_revc.replace('T', 'a')
	seq1_revc = seq1_revc.replace('A', 't')
	seq1_revc = seq1_revc[::-1]
	seq2_revc = seq2.upper()
	seq2_revc = seq2_revc.replace('G', 'c')
	seq2_revc = seq2_revc.replace('C', 'g')
	seq2_revc = seq2_revc.replace('T', 'a')
	seq2_revc = seq2_revc.replace('A', 't')
	seq2_revc = seq2_revc[::-1]
	for i in range(len(seq1_lst)):
		if seq1_lst[i] == seq2_lst[i]:
			seq_score += int(match)
		if not seq1_lst[i] == seq2_lst[i]:
			seq_score += int(mismatch)
	for i in range(len(seq1_lst)):
		if seq1_lst[i] == seq2_revc[i]:
			seq12r_score += int(match)
		if not seq1_lst[i] == seq2_revc[i]:
			seq12r_score += int(mismatch)
	for i in range(len(seq1_lst)):
		if seq1_revc[i] == seq2_lst[i]:
			seq1r2_score += int(match)
		if not seq1_revc[i] == seq2_lst[i]:
			seq1r2_score += int(mismatch)
	for i in range(len(seq1_lst)):
		if seq1_revc[i] == seq2_revc[i]:
			rc2_score += int(match)
		if not seq1_revc[i] == seq2_revc[i]:
			rc2_score += int(mismatch)
	return '2 sequences:', seq_score, '1st sequence, 2nd reverse complement:', seq12r_score, '1st reverse complement, 2nd sequence:', seq1r2_score, 'Both reverse complement:', rc2_score

seq_1 = 'agtctgtca'
seq_2 = 'gatctctgc'

print(match(seq_1, seq_2, 1, -1))
print(match(seq_1, seq_2, 2, -2))

