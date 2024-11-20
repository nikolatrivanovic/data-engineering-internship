import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime


def process_weather_data(input_dir, output_file):
    spark = SparkSession.builder \
        .appName("WeatherDataProcessing") \
        .getOrCreate()

    weather_data = spark.read.csv(
        os.path.join(input_dir, "*"),
        header=True,
        inferSchema=True
    )

    processed_data = weather_data.select(
        col("name").alias("LocationName"),
        from_unixtime(col("time_nano") / 1e9).alias("Timestamp"),
        col("weather_temperature").alias("Temperature_C"),
        (col("weather_windSpeed") * 3.6).alias("WindSpeed_kmh")
    )

    processed_data.coalesce(1).write.csv(output_file, sep=";", header=True, mode="overwrite")
    print(f"Processed data saved to {output_file}")
