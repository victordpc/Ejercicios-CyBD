#!/usr/bin/python
#Victor del Pino

import sys
import re

linea = 0

patron = "Moby"
for line in sys.stdin:
    linea = linea + 1

    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r"\W+", line)

    for word in words:
        if patron == word:
            print(word.lower() + "\t" + str(linea))

