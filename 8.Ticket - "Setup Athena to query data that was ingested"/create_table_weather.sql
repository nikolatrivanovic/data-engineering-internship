CREATE EXTERNAL TABLE IF NOT EXISTS my_db_nt_levi9.weather (
          name STRING,
  time_nano STRING,
  location_latitude STRING,
  location_longitude STRING,
  location_name STRING,
  weather_temperature STRING,
  weather_feelsLike STRING,
  weather_pressure STRING,
  weather_humidity STRING,
  weather_dewPoint STRING,
  weather_clouds STRING,
  weather_windSpeed STRING,
  weather_windDeg STRING,
  weather_windGust STRING,
  no_of_people_visited STRING
        )
            ROW FORMAT SERDE
              'org.apache.hadoop.hive.serde2.OpenCSVSerde'
            WITH SERDEPROPERTIES (
              'escapeChar'='\\',
              'quoteChar'='\"',
              'separatorChar'=',')
            STORED AS INPUTFORMAT
              'org.apache.hadoop.mapred.TextInputFormat'
            OUTPUTFORMAT
              'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
            LOCATION
              's3://processed-data-levi9-nt/pollution'
            TBLPROPERTIES (
              'has_encrypted_data'='false',
              'skip.header.line.count'='1');