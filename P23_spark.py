#!/usr/bin/python
#Victor del Pino

from pyspark import SparkConf, SparkContext
import string
import sys

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('AveragePrice')
sc = SparkContext(conf=conf)

RDDvar = sc.textFile("GOOG.csv")

data = RDDvar.filter(lambda line: "Date" not in line) #ignore first line
stock = data.map(lambda line: (int((line.split(',')[0]).split('-')[0]),float(line.split(',')[4]))) #map (year,price_at_close)
number = data.map(lambda line: (int((line.split(',')[0]).split('-')[0]),1))
aggreg1 = stock.reduceByKey(lambda a, b: a+b)
aggreg2 = number.reduceByKey(lambda a, b: a+b)
union = aggreg1.join(aggreg2)
result = union.map(lambda line: (line[0], line[1][0]/line[1][1]))

result.saveAsTextFile("media.txt")