#!/usr/bin/python
#Victor del Pino

import sys
import re


linea = 0
ignorar = ""

for line in sys.stdin:
    line = re.sub(r'^\W+|\W+$', '', line)  # parsear linea
    numbers = line.split('\t', 4)  # se trocea la linea para obtener los datos
    print(numbers[1] + "\t" + numbers[0])
