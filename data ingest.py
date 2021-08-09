from pyspark.sql import SparkSession
import os
from pyspark.sql import dataframe, SparkSession, SQLContext, HiveContext
from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import Row


session = SparkSession.builder \
    .master("local[*]") \
    .appName("Data-Ingest") \
    .getOrCreate()


df2 = spark.read.option("header",True) \
    .csv("/tmp/resources/trips.csv")

