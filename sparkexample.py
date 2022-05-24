import collections
import numpy

f = open('c:\\SparkCourse\\sample.txt.txt')
lines = f.readlines()
for ratings in lines:
  output = ratings.split()[2]



  for result in output:
    print(result)
