CREATE EXTERNAL TABLE user_activity (
  app_id STRING,
  user_id INT,
  session_id STRING,
  page STRING,
  section STRING,
  event_type STRING,
  country STRING,
  timestamp STRING
)
STORED AS PARQUET
LOCATION '/user_activity/raw';
