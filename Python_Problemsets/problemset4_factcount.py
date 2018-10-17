#!/usr/bin/env

import sys

findfact = sys.argv[1]

findfact = int(findfact)
count = 1
fact = 1

while count <(findfact+1):
	fact *= count	
	count += 1

print(fact)
