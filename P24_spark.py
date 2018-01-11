#!/usr/bin/python
#Victor del Pino


from pyspark import SparkConf, SparkContext
import string
import sys

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('MovieRatings')
sc = SparkContext(conf=conf)

RDDrating = sc.textFile("ratings.csv")
RDDmovies = sc.textFile("movies.csv")

rang = sys.argv[1]
sup_rang = float(rang)
inf_rang = sup_rang - 1.0
moviesData = RDDmovies.filter(lambda line: "movieId" not in line).map(lambda line: (int(line.split(',')[0]), line.split(',')[1]))
ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]), float(line.split(',')[2])))
numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]), 1))
aggreg1 = ratingsData.reduceByKey(lambda a, b: a+b)
aggreg2 = numRatings.reduceByKey(lambda a, b: a+b)
union = aggreg1.join(aggreg2)

avg = union.map(lambda line: (line[0], line[1][0]/line[1][1])).filter(lambda line: line[1] <= sup_rang).filter(lambda line: line[1] >= inf_rang)

union2 = moviesData.join(avg)

result = union2.map(lambda line: (line[1][0], line[1][1]))
result.saveAsTextFile("ratings.txt")