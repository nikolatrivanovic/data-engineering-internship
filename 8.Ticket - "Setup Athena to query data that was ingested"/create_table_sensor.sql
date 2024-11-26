CREATE EXTERNAL TABLE IF NOT EXISTS my_db_nt_levi9.sensor (
  location_latitude STRING,
  location_longitude STRING,
  location_name STRING,
  name STRING,
  pms7003Measurement_pm10Atmo STRING,
  pms7003Measurement_pm25Atmo STRING,
  pms7003Measurement_pm100Atmo STRING,
  bmp280Measurement_temperature STRING,
  bmp280Measurement_pressure STRING,
  dht11Measurement_humidity STRING,
  no_of_people_visited STRING
)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  'separatorChar'=',',
  'quoteChar'='"',
  'escapeChar'='\\'
)
STORED AS TEXTFILE
LOCATION 's3://processed-data-levi9-nt/sensor'
TBLPROPERTIES (
  'skip.header.line.count'='1'
);
