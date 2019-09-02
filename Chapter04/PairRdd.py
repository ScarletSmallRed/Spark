from pyspark import SparkContext

sc = SparkContext( 'local', 'test')
lines = sc.textFile('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter04/Words.txt')
pairRDD = lines.flatMap(lambda line: line.split(' ')).map(lambda word: (word, 1))
print('*' * 100)
pairRDD.foreach(print)


list = ['Hadoop', 'Spark', 'Hive', 'Spark']
rdd = sc.parallelize(list)
pairRDD = rdd.map(lambda word: (word, 1))
print('*' * 100)
pairRDD.foreach(print)