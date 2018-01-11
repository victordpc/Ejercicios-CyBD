#!/usr/bin/python
#Victor del Pino

import sys

previous = None

result = ""
word = ""
line = 0
for line in sys.stdin:
    # line = line.sub(r'^\W+|\W+$', '', line)
    word, line = line.split('\t')
    result = result + line + " "

print(word + ' ' + result)
