# RDD Programming Foundation
## Transformation Operation
Read text files in the HDFS file system and perform basic filter, map, flatmap, groupByKey and reduceByKey operations (code [here](./RDD1.py)).
## Action Operation
Due to the lazy mechanism, the rdd will not actually execute until the **action operation** code is executed (code [here](./ActionOperation.py)).
## Endurance
Key point:
```Python
rdd.cache()
```