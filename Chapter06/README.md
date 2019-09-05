# Chapter 06 Spark SQL
## DataFrame Creation
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