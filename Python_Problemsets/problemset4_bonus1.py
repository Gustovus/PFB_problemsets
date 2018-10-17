#!/usr/bin/env

import sys
import random

seq = sys.argv[1]

seq_list = list(seq)

for i in range(len(seq_list)):
	A = random.randrange(len(seq_list))
	B = random.randrange(len(seq_list))
	seq_list[A], seq_list[B] = seq_list[B], seq_list[A]
print(''.join(seq_list))
