#!/usr/bin/env python3

file_fast = open("Python_06.fastq", "r")

line_count = 0
total_nts = 0

for line in file_fast:
	line_count += 1
	total_nts += len(line)

print(line_count, total_nts, (total_nts/line_count))	
