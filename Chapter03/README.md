# Chapter 03 Spark Environment Construction and Use Method
##  Develop a Spark Standalone Application
Perform word frequency statistics on the file, [Text](./Text.txt) in the local file system and relevant code [here](./WordCount.py).

Next, we upload the [Text.txt](./Text.txt) file in the local file system to the distributed file system HDFS (put it to the hadoop user directory):
```shell
$ hadoop fs -put <localsrc> ... <dst>
```
And Relevant code [here](./WordCountHDFS.py).