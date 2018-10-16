#!/usr/bin/env python3
import sys

num = int(sys.argv[1])

if num > 0:
	print("Positive")
	if num > 50:
		print("WOW! This is a large number")
		if num % 3 == 0:
			print("This number is larger than 50 and divisible by 3, WOW")
	elif num == 50:
		print("This number is exactly 50, impressive")
	else:
		if num % 2 == 0:
			print("This is a even number that is smaller than 50")
elif num < 0:
	print("Negative")
else:
	print("Fucking 0")
