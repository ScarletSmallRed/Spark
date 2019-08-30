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