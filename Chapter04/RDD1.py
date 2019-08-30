from pyspark import SparkContext
sc = SparkContext( 'local', 'test')
file_path = 'hdfs://localhost:9000/user/hadoop/Text.txt'
text = sc.textFile(file_path)
print('*' * 100)
print(text.first())

# Filter
lines = text.filter(lambda line: 'and' in line)
lines.foreach(print)

# Map
data = [1, 2, 3, 4, 5]
rdd1 = sc.parallelize(data)
rdd2 = rdd1.map(lambda x: x + 10)
rdd2.foreach(print)

words = text.map(lambda line: line.split(' '))
words.foreach(print)

# FlatMap
print('*' * 100)
words = text.flatMap(lambda line: line.split(' '))
words.foreach(print)

# GroupByKey
print('*' * 100)
words = sc.parallelize([('Hadoop', 1), ('is', 1), ('good', 1), ('Spark', 1), ('is', 1), ('fast', 1), ('Spark', 1), ('is', 1), ('better', 1)])
words1 = words.groupByKey()
words1.foreach(print)

# ReduceMap
print('*' * 100)
word1 = words.reduceByKey(lambda a, b: a + b)
word1.foreach(print)