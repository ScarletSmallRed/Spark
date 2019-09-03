from pyspark import SparkContext

sc = SparkContext( 'local', 'test')
list = [('Hadoop', 1), ('Spark', 1), ('Hive', 1), ('Spark', 1)]
print('*' * 100)
pairRdd = sc.parallelize(list)
pairRdd.reduceByKey(lambda a, b: a + b).foreach(print)


pairRDD = sc.parallelize(list)
print('*' * 100)
print(pairRdd.groupByKey())
pairRDD.groupByKey().foreach(print)


words = ['one', 'two', 'two', 'three', 'three', 'three']
wordPairsRDD = sc.parallelize(words).map(lambda word: (word, 1))

reduce_word = wordPairsRDD.reduceByKey(lambda a, b: a + b)
print('*' * 100)
reduce_word.foreach(print)


group_word = wordPairsRDD.groupByKey().map(lambda t: (t[0], sum(t[1])))
print('*' * 100)
group_word.foreach(print)