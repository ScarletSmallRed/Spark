from pyspark import SparkContext

sc = SparkContext( 'local', 'test')

text_file = sc.textFile('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter05/Word.txt')
print('*' * 100)
print(text_file.first())

# text_file.saveAsTextFile('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter05/WriteBack')
text_file = sc.textFile('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter05/WriteBack')
print('*' * 100)
print(text_file)


text_file = sc.textFile('hdfs://localhost:9000/user/hadoop/Word.txt')
print('*' * 100)
print(text_file.first())

# text_file.saveAsTextFile('hdfs://localhost:9000/user/hadoop/WriteBack')
text_file = sc.textFile('hdfs://localhost:9000/user/hadoop/WriteBack')
print('*' * 100)
print(text_file.first())