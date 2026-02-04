# Real-Time Web Analytics Platform (Dockerized Big Data Pipeline)

## Overview

This project implements an **end-to-end real-time web analytics system** using modern big data technologies, fully containerized using **Docker and Docker Compose**.

A dummy **Flask application** simulates browser analytics events (page views, clicks, scrolls, etc.).  
These events are streamed into **Apache Kafka**, processed by **multiple streaming frameworks**, and stored in **HDFS-based analytical storage**.

The system runs as a **Docker-based pseudo distributed cluster**, including **2 HDFS DataNodes (slave nodes)**.

---

## Objectives

- Simulate real-time web analytics events
- Use Kafka as a **central event streaming platform**
- Persist **raw Kafka events** for durability and replay
- Perform **real-time analytics and aggregations**
- Store data using **big data tools implemented on HDFS**
- Run the entire system using **Docker (no local installations)**

---

## High-Level Architecture
```tree
+----------------------+
|  Flask App (Docker)  |
+----------+-----------+
           |
           v
+----------+-----------+
|     Apache Kafka     |
+----------+-----------+
           |
           +----------------------+
           |                      |
           v                      v
+----------+-----------+  +-------+--------+
|   Apache Storm       |  |   Apache Spark |
+----------+-----------+  +-------+--------+
           |                      |
           v                      v
+----------+-----------+  +-------+--------+
|  HDFS                |  |  Hive           |
|  (Raw JSON Data)     |  |  (Aggregations) |
+----------------------+  +-----------------+
```

### Architecture Rationale
- **Kafka** acts as the single source of truth
- **Storm** continuously drains Kafka and stores immutable raw events
- **Spark Structured Streaming** performs analytics and aggregations
- **Hive** provides SQL-based analytics on top of HDFS
- **HDFS replication factor = 2** ensures fault tolerance

---

## Technologies Used

| Layer | Technology |
|-----|-----------|
| Event Producer | Flask (Python) |
| Messaging | Apache Kafka |
| Coordination | Apache Zookeeper |
| Raw Stream Storage | Apache Storm |
| Stream Processing | Apache Spark Structured Streaming |
| Distributed Storage | HDFS (2 DataNodes) |
| Analytics Storage | Apache Hive |
| Orchestration | Docker & Docker Compose |

---

## Project Structure

```tree
web_analytics/
│
├── docker-compose.yml
├── .env
├── README.md
│
├── flask-app/
│    ├── Dockerfile
│    ├── requirements.txt
│    └── app.py
│
├── kafka/
│    ├── create-topics.sh
│    └── server.properties
│
├── storm/
│    ├── Dockerfile
│    └── topology.py
│
├── spark/
│    ├── Dockerfile
│    └── kafka_to_hive.py
│
├── hdfs/
│    └── hdfs-site.xml
│
├── hive/
│    ├── hive-site.xml
│    └── ddl/
│         ├── raw_web_events.sql
│         └── page_analytics.sql
│
└── scripts/
     ├── init_hdfs.sh
     └── init_hive.sh
```

---

## Design Decisions

### Kafka
- Decouples producers and consumers
- Supports multiple independent streaming pipelines
- Enables replay and fault tolerance

### Storm (Raw Storage Path)
- Low-latency, always-on streaming
- Writes **immutable raw events** directly to HDFS
- Enables reprocessing and auditing

### Spark Structured Streaming
- Rich transformation and aggregation capabilities
- Native Kafka integration
- Ideal for window-based analytics

### Hive
- SQL-based analytics layer
- Stores data in ORC/Parquet format on HDFS
- Industry-standard data warehouse solution

---

## Docker Strategy

### Runs inside containers
- Kafka & Zookeeper
- Storm Nimbus & Supervisors
- Spark Master & Workers
- HDFS NameNode & DataNodes
- Hive Metastore & Server2
- Flask App

### Custom Dockerfiles
- Flask app (event producer)
- Spark streaming job
- Storm topology

### Official Docker Images
- Kafka
- Zookeeper
- HDFS
- Hive

---

## Data Flow

### 1 Event Generation
- Flask app simulates user behavior
- JSON events are published to Kafka topic `web_analytics`

### 2 Raw Data Persistence
- Storm consumes Kafka
- Writes raw JSON events to HDFS
- /raw/web_analytics/date=YYYY-MM-DD/

### 3 Analytics Processing
- Spark consumes Kafka independently
- Parses and validates events
- Performs window-based aggregations
- Writes results to Hive tables

---

## Hive Tables

### Raw Events
```sql
CREATE TABLE raw_web_events (
  event_id STRING,
  user_id STRING,
  session_id STRING,
  event_type STRING,
  page_url STRING,
  browser STRING,
  os STRING,
  country STRING,
  event_time TIMESTAMP
)
STORED AS ORC;

```
### Aggregated Analytics

```sql
CREATE TABLE page_analytics (
  page_url STRING,
  event_type STRING,
  event_count BIGINT,
  window_start TIMESTAMP,
  window_end TIMESTAMP
)
STORED AS ORC;
```
## How to Run
- start cluster
```bash
 docker compose up -d
```
- create kafka topic
```bash
docker exec kafka bash /create-topics.sh
```
- initialize HDFS
```bash
docker exec namenode bash /scripts/init_hdfs.sh
```
- Initialize Hive tables
```bash
docker exec hive-server bash /scripts/init_hive.sh
```

## Sample Queries
### Most Viewed Pages
```sql 
SELECT page_url, COUNT(*) AS views
FROM raw_web_events
WHERE event_type = 'page_view'
GROUP BY page_url
ORDER BY views DESC;
```
### Events Per Minute
```sql
SELECT window_start, SUM(event_count)
FROM page_analytics
GROUP BY window_start
ORDER BY window_start;
```
