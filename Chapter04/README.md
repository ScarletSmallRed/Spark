# RDD Programming Foundation
## Transformation Operation
Read text files in the HDFS file system and perform basic filter, map, flatmap, groupByKey and reduceByKey operations (code [here](./RDD1.py)).
## Action Operation
Due to the lazy mechanism, the rdd will not actually execute until the **action operation** code is executed (code [here](./ActionOperation.py)).
## Endurance
Key point (code [here](./Endurance.py)):
```Python
rdd.cache()
```
## Custom Partitioning Method
Key point (code [here](./Partition.py)):
```Python
data = sc.parallelize(range(10), 5)
data.map(lambda x: (x, 1)).partitionBy(10, MyPartiontioner).map(lambda x: x[0]).saveAsTextFile('file:///')
```
## Key-Value Pair RDD Creation
* Load from file
* Create an RDD from a parallel collection (code [here](./PairRdd.py))
## Common Key-Value Pair RDD Transportation Operations
* GroupByValue
* ReduceByValue (code [here](./Transformation1.py))
* mapValues (code [here](./Transformation2.py))