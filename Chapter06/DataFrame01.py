from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()
df = spark.read.json('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.json')
print('*' * 100)
df.show()

print('*' * 100)
df = spark.read.text('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.txt')
df.show()