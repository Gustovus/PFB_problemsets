#!/usr/bin/env python3

import re

headcrack = open('Python_07.fasta', 'r')

headhunt = headcrack.read()

found = re.findall(r"\>\S+\s", headhunt)
print(found)

