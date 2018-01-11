#!/usr/bin/python
# Victor del Pino

import sys
import re

linea = 0
ignorar = ""

contador = 100
impreso=0
"""
f1 = open('../ext/movies/movies.csv', 'r')

for line in f1:
    if linea == 0:
        re.sub(r'^\W+|\W+$', '', ignorar)
        linea = linea + 1
    else:
        line = re.sub(r'^\W+|\W+$', '', line)  # parsear linea
        numbers = line.split(',', 4)  # se trocea la linea para obtener los datos
        print(numbers[0] + "\t" + numbers[1] + "\t-1")

f1.close()

f2 = open('../ext/movies/ratings.csv', 'r')

for line in f2:
    if linea == 0:
        re.sub(r'^\W+|\W+$', '', ignorar)
        linea = linea + 1
    else:
        line = re.sub(r'^\W+|\W+$', '', line)  # parsear linea
        numbers = line.split(',', 4)  # se trocea la linea para obtener los datos
        print(numbers[1] + "\t-1" + "\t" + numbers[2])


f2.close()
"""
"""
"""
f1 = open('../ext/movies/movies.csv', 'r')
f2 = open('../ext/movies/ratings.csv', 'r')
for line in f1:
    if linea == 0:
        re.sub(r'^\W+|\W+$', '', ignorar)
        linea = linea + 1
    else:
        line = re.sub(r'^\W+|\W+$', '', line)  # parsear linea
        numbers = line.split(',', 4)  # se trocea la linea para obtener los datos

        linea2 = 0
        for line2 in f2:
            if linea2 == 0:
                re.sub(r'^\W+|\W+$', '', ignorar)
                linea2 = linea2 + 1
            else:
                line2 = re.sub(r'^\W+|\W+$', '', line2)  # parsear linea
                numbers2 = line2.split(',', 4)  # se trocea la linea para obtener los datos

                if numbers[0] == numbers2[1]:
                    print(numbers[1] + "\t" + numbers2[2])
                    impreso = 1
        f2.seek(0)
        if impreso == 0:
            print(numbers[0] + "\t" + numbers[1] + "\t-1")
        impreso = 0

f1.close()
f2.close()
"""
"""

"""
for line in sys.stdin:
    if linea == 0:
        re.sub(r'^\W+|\W+$', '', ignorar)
        linea = linea + 1
    else:
        line = re.sub(r'^\W+|\W+$', '', line)  # parsear linea
        numbers = line.split(',', 4)  # se trocea la linea para obtener los datos
        print(numbers[1] + "\t" + numbers[2])
"""