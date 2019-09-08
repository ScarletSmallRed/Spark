from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()
df = spark.read.json('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.json')
print('*' * 100)
df.show()

print('*' * 100)
df = spark.read.text('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.txt')
df.show()

print('*' * 100)
people_df = spark.read.json('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.json')
# people_df.select('name').write.format('json').save('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/PeopleDF1.json')
people_df.select('age').write.format('text').save('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/PeopleDF1.txt')