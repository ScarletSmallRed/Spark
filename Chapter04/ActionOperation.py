from pyspark import SparkContext
sc = SparkContext( 'local', 'test')

rdd = sc.parallelize([1, 2, 3, 4, 5])
print('*' * 100)
print(rdd.count())
print(rdd.first())
print(rdd.take(3))
print(rdd.reduce(lambda a, b: a + b))
print(rdd.collect())
print(rdd.foreach(lambda elem: print('* {}'.format(elem))))