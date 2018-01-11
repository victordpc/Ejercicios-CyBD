#!/usr/bin/python
#Victor del Pino

import sys

previous = None
movies = ""
note1 = []
note2 = []
note3 = []
note4 = []
note5 = []

for line in sys.stdin:
    key, value = line.split('\t')
    indice = float(key)

    if indice < 1.0:
        note1.append(value)
    elif indice < 2.0:
        note2.append(value)
    elif indice < 3.0:
        note3.append(value)
    elif indice < 4.0:
        note4.append(value)
    elif indice < 5.0:
        note5.append(value)

print("(1) 1 or lower")
for i in note1:
    print(i)

print("(2) 2 or lower (but higher than 1)")
for i in note2:
    print(i)
print("")

print("(3) 3 or lower (but higher than 2)")
for i in note3:
    print(i)
print("")

print("(4) 4 or lower (but higher than 3)")
for i in note4:
    print(i)
print("")

print("(5) 5 or lower (but higher than 4)")
for i in note5:
    print(i)
print("")
