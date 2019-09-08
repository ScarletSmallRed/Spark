from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()
df = spark.read.json('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.json')
print('*' * 100)
df.show()

print('*' * 100)
df.printSchema()
df.select(df['name'], df['age']).show()
df.select(df['name'], df['age'] + 1).show()
df.filter(df['age'] > 20).show()
df.groupBy('age').count().show()
df.sort(df['age'].desc()).show()
df.sort(df['age'].desc(), df['name'].asc()).show()
df.sort(df['age'].desc(), df['name'].desc()).show()