#!/usr/bin/env python3

import sys

checknumber = sys.argv[1]

if int(checknumber) > 0:
	print("Positive number")
else:
	print("Not a positive number")
