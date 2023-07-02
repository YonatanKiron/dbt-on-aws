from os import environ
import sys
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .config("hive.metastore.uris", "thrift://spark-thrift-server-service:10001") \
    .getOrCreate()
spark.sql("SHOW DATABASES").show()
spark.stop()
