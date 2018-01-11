#!/usr/bin/python
# Victor del Pino

import sys

import sys

previous = None
suma = 0.0
elementos = 0

for line in sys.stdin:
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            media = suma / elementos
            elementos = 0
            print(previous + "\t" + str(media))
        previous = key
        suma = 0.0

    suma = suma + float(value)
    elementos = elementos + 1
media = suma / elementos
print(previous + "\t" + str(media))
