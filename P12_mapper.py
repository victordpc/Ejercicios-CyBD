#!/usr/bin/python
#Victor del Pino

import sys
import re

siguiente = False

for line in sys.stdin:
    # Partimos la entrada en palabras
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)

    # Recorremos las palabras hasta que encontramos la peticion (Get | Post)
    # y nos quedamos con la siguiente palabra que es la url
    for words in words:
        if siguiente:
            print(words.lower() + "\t1")
            siguiente = False
        if words =="GET" or words == "POST":
            siguiente = True