```
bigdata-user-analytics/
├── docker-compose.yml
├── flask/
│   ├── app1/
│   │   ├── app.py
│   │   └── Dockerfile
│   ├── app2/
│   └── app3/
├── kafka/
├── spark/
│   ├── streaming_job.py
│   └── Dockerfile
├── hdfs/
├── hive/
│   ├── ddl.hql
│   └── analytics.hql
├── airflow/
│   ├── dags/
│   │   └── hive_daily_analytics.py
├── streamlit/
│   ├── app.py
│   └── Dockerfile
└── README.md
```
- created flask/app/app.py
- ZooKeeper:
  - Manages Kafka metadata
  - Broker coordination

You do not write code for ZooKeeper.

- Spark Structured Streaming (Core Processing)
  - Read Kafka events
  - Parse JSON
  - Write to HDFS in parquet format
  - spark/streaming_job.py
-  HDFS (Distributed Storage)
  - Data layout:
    - /user_activity/raw/
    - /user_activity/aggregated/
-  Hive (Batch Analytics Layer)
  -  SQL analytics on historical data
  -  Create summary tables
___
**hive/ddl.hql**
```sql
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




```
**hive/analytics.hql**
```sql
CREATE TABLE daily_page_visits AS
SELECT
  page,
  COUNT(*) AS visits
FROM user_activity
GROUP BY page;

```
___
### Why Hive Results Exist (Very Important)

Hive does not print results to UI.

Instead, it:

- Creates analytics tables
- Stores results in HDFS
- Streamlit reads those tables

### Airflow (Scheduling Hive Queries)

Automate analytics generation.
**airflow/dags/hive_daily_analytics.py**