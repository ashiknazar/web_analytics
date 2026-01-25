# Real-Time User Activity Monitoring Big Data Platform (Extended)

## 1. Real-Life Problem Being Solved

Modern web applications need to monitor user activity in real time to understand:

- How many users are active
- What actions users perform
- Whether errors or performance issues are occurring
- Which pages or sections drive engagement
- How users navigate internally across the application
- Where users are coming from geographically

This project simulates a realistic scenario to study **user behavior analytics**, **system performance**, **stream processing**, and **predictive insights**.

---

## 2. Data Sources

### 2.1 User Activity Events (Primary Stream)

- 3 Flask applications running concurrently
- Each Flask app simulates 10 concurrent users
- Each user continuously generates structured webpage activity events

These Flask applications act as **synthetic event producers**, mimicking real-world user interactions.

---

### 2.2 Application Logs (Secondary Stream)

- Flask access logs
- Error logs
- Performance logs

These logs are treated separately from user events to demonstrate **log ingestion pipelines**.

Optionally, **Apache Sqoop** imports mock user profile data from an RDBMS into Hive for enriched analytics.

---

## 3. Event Data Schema (Streamed)

Each event represents **one user interaction** on a webpage.

(unchanged JSON schema)

---

## 4. Complete Tool Stack & Responsibilities

| Layer | Tool | Purpose in This Project |
|------|------|-------------------------|
| Data Generation | Flask (3 instances) | Simulate concurrent users generating real-time activity events |
| Log Ingestion | **Apache Flume** | Collect Flask application logs and deliver them reliably to HDFS |
| Event Ingestion & Buffering | **Apache Kafka** | High-throughput ingestion and buffering of user activity events |
| Coordination | ZooKeeper / KRaft | Metadata management and coordination for Kafka, Storm, HBase |
| Real-Time Processing | **Apache Storm** | Low-latency, per-event processing (alerts, live counters, session tracking) |
| Stream Analytics | Spark Streaming | Near-real-time aggregation using micro-batches |
| Batch Processing | Apache Spark (Batch) | ETL, joins, and daily aggregations |
| Batch ETL | Apache Pig | Normalize raw HDFS data into Hive-ready format |
| Storage | HDFS | Store raw events, logs, and processed datasets |
| NoSQL Storage | HBase | Low-latency access to per-user and per-session data |
| Query & Analytics | Apache Hive | SQL-based analytics for dashboards |
| RDBMS Integration | Apache Sqoop | Import mock relational user profile data |
| Machine Learning | Apache Mahout | Clustering and recommendation algorithms |
| Workflow Orchestration | Apache Airflow | Schedule Spark, Hive, Pig, and Sqoop jobs |
| Visualization | Streamlit | Dashboards for real-time and historical insights |
| Resource Management | YARN | Allocate resources for Spark jobs |
| Containerization | Docker & Docker Compose | Simulate a multi-node Big Data cluster |

---

## 5. System Architecture

### 5.1 Data Ingestion

```tree

Flask Apps
├── User Activity Events → Kafka
└── Application Logs → Flume → HDFS (/logs)
```


---

### 5.2 Processing Layer

```tree

Kafka
├── Apache Storm → HBase (real-time views, alerts)
└── Spark Streaming → HDFS (aggregated metrics)
```

- **Storm** handles sub-second processing such as:
  - Active user counts
  - Error spikes
  - Session navigation tracking

- **Spark Streaming** handles windowed aggregations and metrics.

---

### 5.3 Batch Analytics & Storage

```tree
HDFS
├── Spark Batch / Pig → Hive
└── Raw Logs (from Flume)
```


- Daily summaries
- Navigation path analysis
- Geographic distribution
- Enriched analytics using Sqoop-imported data

---

### 5.4 Analytics, ML & Visualization

- Hive provides analytical tables
- Mahout performs clustering and recommendations
- Streamlit visualizes KPIs
- Airflow orchestrates workflows

---

## 6. Example Metrics Produced

| Metric | Source |
|------|-------|
| Most visited pages | Hive |
| Section engagement | Hive |
| Navigation paths | Hive |
| Geographic traffic | Hive |
| Live active users | Storm → HBase |
| Recent pages per user | HBase |
| Error rate anomalies | Storm |
| Recommendations | Mahout |

---

## 7. Project Abstract

This project demonstrates an end-to-end **Big Data ecosystem** for real-time user activity monitoring:

- **Flask** generates synthetic user events and logs
- **Flume** ingests application logs into HDFS
- **Kafka** buffers high-velocity event streams
- **Storm** performs low-latency real-time processing
- **Spark Streaming & Batch** handle analytics and ETL
- **HDFS & HBase** store analytical and real-time data
- **Hive** enables SQL-based insights
- **Mahout** adds predictive capabilities
- **Airflow** automates workflows
- **Streamlit** provides dashboards
- **YARN & ZooKeeper** manage cluster resources and coordination

This architecture intentionally separates **logs vs events**, **real-time vs batch**, and **low-latency vs analytical workloads**, reflecting real-world Big Data system design.
