#!/usr/bin/env

import sys

start = sys.argv[1]
end = sys.argv[2]

start = int(start)
end = int(end)

for num in range(start, end+1):
	if num % 2 != 0:
		print(num)

