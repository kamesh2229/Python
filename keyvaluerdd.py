def parseLine(line):
    fields = line.split(',')
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)

## output of above program ###

## 33, 385 ##
##   33,2 ##
##  55,221 ##
##   40,465 ##

totalsByAge = rdd.mapValues(lambda x : (x,1)).reduceByKey(lambda x,y: (x[0] + y[0], x[1] + y[1]))

rdd,mapValues(lambda x : (x,1))

## Output ##

## 33, 385 = (33, (385,1))
## 33, 2 = (33, (2,1))

reduceByKey(lambda x,y: (x[0] + y[0], x[1] + y[1]))

## Adds up all values for unique keys ##

(33, (387,2))

