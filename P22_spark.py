#!/usr/bin/python
#Victor del Pino

from pyspark import SparkConf, SparkContext
import string
import sys
import re

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('URLaccess')
sc = SparkContext(conf=conf)

RDDvar = sc.textFile("access_log")

words = RDDvar.map(lambda line: (line.split('"')[1]))

domines = words.map(lambda line: line.split('/')).filter(lambda line: len(line) > 1).map(lambda line: (str(line[1]), 1))
aggreg1 = domines.reduceByKey(lambda a, b: a+b)

aggreg1.saveAsTextFile("access.txt")