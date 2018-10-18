#!/usr/bin/env python3

file_tom = open("Python_06.txt", "r")
file_tomw = open("Python_06_uc.txt", "w")
for line in file_tom:
	line = line.rstrip()
	print(line.upper())
	file_tomw.write(str(line.upper()) + '\n')

file_tom.close()
file_tomw.close()
