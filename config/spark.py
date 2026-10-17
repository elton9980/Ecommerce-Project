from pyspark.sql import SparkSession

spark = (SparkSession.builder 
    .appName("ProjectApp") 
    .master("local[*]")
    .getOrCreate()
)



