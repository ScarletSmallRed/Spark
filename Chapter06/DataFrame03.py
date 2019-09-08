from pyspark.sql.types import Row
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType

sc = SparkContext( 'local', 'test')
spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()

people = sc.textFile('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.txt').map(lambda line : line.split(',')).map(lambda p: Row(name = p[0], age = int(p[1])))
schema_people = spark.createDataFrame(people)
schema_people.createOrReplaceTempView("people")
persons_df = spark.sql("select * from people where age > 20")
persons_rdd = persons_df.rdd.map(lambda t : "Name:"+t['name']+", "+"Age:"+str(t['age']))
print('*' * 100)
persons_df.show()
persons_rdd.foreach(print)


schema_str = 'name age'
fields = [StructField(field_name, StringType(), nullable = True) for field_name in schema_str.split(' ')]
schema = StructType(fields)
people = sc.textFile('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter06/People.txt').map(lambda line : line.split(',')).map(lambda p: Row(p[0], p[1].strip()))
schema_people = spark.createDataFrame(people, schema)
print('*' * 100)
print(type(schema_people))
schema_people.createOrReplaceTempView("people1")
results = spark.sql("select name, age from people1 where age > 20")
print(type(results))
results.show()