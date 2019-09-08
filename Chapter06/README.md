# Chapter 06 Spark SQL
## [DataFrame Basic Opeartions](./DataFrame01.py)
* Creation
```Python
spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()
```
* Read json file
```Python
df = spark.read.json()
```
* Read text file
```Python
df = spark.read.text()
```
* Save file
```Python
people_df.select('name').write.format('json').save('')
people_df.select('age').write.format('text').save('')
```
## [DataFrame Common Operations](./DataFrame02.py)
* printSchema()
* select()
* filter()
* groupBy()
* sort()
## RDD to DataFrame Conversion
* Inferring RDD mode by using reflection mechanism
* Programmatically define RDD mode

Relevant code [here](./DataFrame03.py).