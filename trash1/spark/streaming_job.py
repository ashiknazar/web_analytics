from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("UserActivityStreaming") \
    .getOrCreate()

schema = StructType([
    StructField("app_id", StringType()),
    StructField("user_id", IntegerType()),
    StructField("session_id", StringType()),
    StructField("page", StringType()),
    StructField("section", StringType()),
    StructField("event_type", StringType()),
    StructField("country", StringType()),
    StructField("timestamp", StringType())
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "user_events") \
    .load()

parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

query = parsed.writeStream \
    .format("parquet") \
    .option("path", "hdfs://namenode:8020/user_activity/raw") \
    .option("checkpointLocation", "/tmp/checkpoints") \
    .start()

query.awaitTermination()
