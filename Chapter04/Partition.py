from pyspark import SparkContext, SparkConf

def MyPartiontioner(key):
    print('MyPationer is running')
    print('The key is {}'.format(key))
    return key % 10

def main():
    print('The main function is running')
    conf = SparkConf().setMaster('local').setAppName('MyApp')
    sc = SparkContext(conf = conf)
    data = sc.parallelize(range(10), 5)
    data.map(lambda x: (x, 1)).partitionBy(10, MyPartiontioner).map(lambda x: x[0]).saveAsTextFile('file:///Users/shenshaohong/Documents/GitHub/Spark/Chapter04/Text.txt')

if __name__ == "__main__":
    main()