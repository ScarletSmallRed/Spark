from pyspark import SparkContext
sc = SparkContext( 'local', 'test')

list = ['Hadoop', 'Spark', 'Hive']
rdd = sc.parallelize(list)
rdd.cache()
print(rdd.count())
print(rdd.collect())
print(', '.join(rdd.collect()))