from pyspark.sql import SparkSession

spark = (SparkSession.builder 
    .appName("ProjectApp") 
    .master("local[*]")
    .getOrCreate()
)



spark.sql("CREATE DATABASE IF NOT EXISTS bronze")