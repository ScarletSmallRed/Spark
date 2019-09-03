from pyspark import SparkContext

sc = SparkContext( 'local', 'test')
list = [('Spark', 2), ('Hadoop', 6), ('Hadoop', 4), ('Spark', 6)]
rdd = sc.parallelize(list)
rdd = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])).mapValues(lambda x: (x[0] / x[1]))
print('*' * 100)
rdd.foreach(print)
print(rdd.collect())