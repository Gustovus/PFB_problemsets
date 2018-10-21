#!/usr/bin/env python3

class DNAseq(object):
	
	def __init__(self, seq, gName, spName):
		self.seq = seq
		self.gName = gName
		self.spName = spName
	
	def lenSeq(self):
		leng = len(self.seq)
		return leng

	def nucComp(self):
		countA = self.seq.count('A')
		countT = self.seq.count('T')
		countC = self.seq.count('C')
		countG = self.seq.count('G')
		return ['A:' + str(countA), 'T:' + str(countT), 'C:' + str(countC), 'G:' + str(countG)]

	def GCcont(self):
		countG = self.seq.count('G')
		countC = self.seq.count('C')
		leng = len(self.seq)
		return ((countG + countC)/leng)

	def FASTAform(self):
		return '>' + self.gName + '\n' + self.seq 


DNAseq_obj1 = DNAseq('ATCGATAGCGATTT', 'ABC1', 'Drosophila melanogaster')

for d in [DNAseq_obj1]:
	print('Gene Name:', d.gName, '', 'Sequence:', d.seq)
	print(d.lenSeq())
	print(d.nucComp())
	print(d.GCcont())
	print(d.FASTAform())

