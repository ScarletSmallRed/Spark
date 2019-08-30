from pyspark import SparkContext
sc = SparkContext( 'local', 'test')
logFile = "file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter03/Text.txt"

logData = sc.textFile(logFile, 2).cache()
numAs = logData.filter(lambda line: 'is' in line).count()
numBs = logData.filter(lambda line: 'and' in line).count()
print('Lines with is: %s, Lines with and: %s' % (numAs, numBs))