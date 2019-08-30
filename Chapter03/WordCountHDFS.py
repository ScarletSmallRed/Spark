from pyspark import SparkContext
sc = SparkContext( 'local', 'test')
file_path = 'hdfs://localhost:9000/user/hadoop/Text.txt'
text_file = sc.textFile(file_path)
print('*' * 100)
print(text_file.first())
word_count = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a, b : a + b)
word_count.foreach(print)