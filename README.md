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

## 2. Data Source

### Data Source Design

- 3 Flask applications running concurrently
- Each Flask app simulates 10 concurrent users
- Each user generates webpage activity events continuously

These Flask applications act as **synthetic data producers**, mimicking real-world user interactions.  
Optionally, **Sqoop** can import additional mock user profile data from a relational database into Hive for enriched analytics.

---

## 3. Event Data (Streamed Schema)

Each event represents **one user interaction** on a webpage.  

The schema includes:

- User info (user ID, session ID, logged-in status)
- Geolocation (country, state, city)
- Page navigation (current page, previous page, next page, referrer)
- Section/portion of page interaction
- Event type and target (click, view, scroll, etc.)
- Timing (event timestamp, time spent on page)
- Performance metrics (response time, status)

This allows tracking:

- Page visits and section-level interactions
- Internal navigation (previous → current → next page)
- User location and session info
- Interaction performance metrics
- Time spent on each page or section

### Sample User Activity Event (JSON)

```json
{
  "app_id": "flask_app_1",
  "user": {
    "user_id": 4,
    "session_id": "fa1_sess_4",
    "is_logged_in": true
  },
  "geo": {
    "country": "India",
    "state": "Karnataka",
    "city": "Bangalore"
  },
  "page": {
    "current_page": "/products",
    "previous_page": "/home",
    "next_page": "/checkout",
    "referrer": "google_search"
  },
  "section": {
    "section_id": "product_list",
    "component": "recommendation_grid",
    "position": "middle"
  },
  "event": {
    "event_type": "click",
    "target": "add_to_cart_btn"
  },
  "timing": {
    "event_time": "2026-01-16T18:10:12",
    "time_on_page_ms": 15340
  },
  "performance": {
    "response_time_ms": 240,
    "status": "success"
  }
}

```
## 4. Complete Tool Stack & Implementation
```
| Layer                  | Tool                    | Purpose & Implementation in Project                                                                                                             |
| ---------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Generation        | Flask (3 instances)     | Simulate multiple concurrent users generating activity events in JSON format                                                                    |
| Streaming Ingestion    | Apache Flume            | Collect events from Flask apps and reliably deliver them to Kafka and/or HDFS                                                                   |
| Streaming & Buffering  | Apache Kafka            | Ingest high-velocity event streams, act as a message broker for Spark Streaming                                                                 |
| Coordination           | ZooKeeper / KRaft       | Maintain Kafka cluster metadata, broker leadership, and consumer group coordination                                                             |
| Storage                | HDFS                    | Store raw events and processed datasets for batch analytics                                                                                     |
| NoSQL Storage          | HBase                   | Store individual events for low-latency queries like “last 5 pages visited by user X”                                                           |
| Processing Engine      | Apache Spark            | - Streaming: Real-time aggregation of page visits, section clicks, navigation paths <br> - Batch: Daily summaries and ETL transformations       |
| Batch ETL              | Apache Pig              | Preprocess HDFS raw logs, normalize fields, and convert to Hive-ready format                                                                    |
| Resource Management    | YARN                    | Allocate CPU/memory for Spark executors, schedule streaming and batch jobs across nodes (Docker containers)                                     |
| Query & Analytics      | Apache Hive             | Create aggregated tables: page metrics, section engagement, navigation paths, geographic distribution; results consumed by Streamlit dashboards |
| RDBMS Integration      | Apache Sqoop            | Import mock user data from relational databases for enriched analytics                                                                          |
| Machine Learning       | Apache Mahout           | Run clustering or recommendation algorithms (e.g., product recommendations based on clicks)                                                     |
| Workflow Orchestration | Apache Airflow          | Schedule Spark, Hive, Pig, and Sqoop workflows to update tables daily/hourly automatically                                                      |
| Visualization          | Streamlit               | Display precomputed analytics: bar charts for most visited pages, line charts for daily active users, maps for geographic distribution          |
| Containerization       | Docker & Docker Compose | Simulate multi-node Big Data cluster on a single machine with independent containers                                                            |
```
## 5. System Architecture

The system architecture includes:

#### 1.Data Generation & Ingestion
 - Flask apps → Flume agents → Kafka → HDFS
 - Sqoop imports mock relational user data

#### 2.Processing
 - Spark Streaming consumes Kafka events for real-time analytics
 - Spark batch jobs run ETL and aggregation periodically
 - Pig scripts preprocess raw HDFS data for Hive tables

#### Storage

 - HDFS stores raw and batch-processed data
 - HBase stores low-latency, user-level event access

#### Analytics & Workflow
 - Hive queries summarize daily metrics (pages, sections, navigation paths, geo-distribution)
 - Mahout performs clustering/recommendations
 - Airflow schedules all Spark, Hive, Pig, and Sqoop jobs

#### Visualization
 - Streamlit dashboards consume Hive/HBase tables for real-time and historical insights

#### Coordination & Resource Management
 - ZooKeeper coordinates Kafka brokers and HBase region servers
 - YARN manages Spark executor resources across nodes (Docker containers)

```
| Metric              | Example Output                                      | Source                               |
| ------------------- | --------------------------------------------------- | ------------------------------------ |
| Most Visited Pages  | /products → 12,450 visits <br> /home → 9,830 visits | Hive table: page_metrics_daily       |
| Section Engagement  | recommendation_grid → 6,120 interactions            | Hive table: section_engagement_daily |
| Navigation Paths    | /home → /products → /checkout (3,210 users)         | Hive table: navigation_paths_daily   |
| Geographic Traffic  | India, Karnataka, Bangalore → 5,200 users           | Hive table: geo_traffic_daily        |
| Last Pages per User | user_id 4 → /home → /products                       | HBase                                |
| Recommendations     | Suggest products from most-clicked sections         | Mahout                               |
```

## 7. Project Abstract

This project implements a full Big Data ecosystem workflow for real-time user activity monitoring, including:

- Data generation: Synthetic user activity streams using Flask
- Streaming ingestion: Flume and Kafka for reliable event transport
- Processing: Spark Streaming & batch for aggregation; Pig for ETL
- Storage: HDFS for raw/aggregated data; HBase for fast lookups
- Analytics: Hive for SQL-based metrics, Mahout for predictive insights
- Automation: Airflow schedules Spark, Hive, Pig, and Sqoop jobs
- Visualization: Streamlit dashboards for end-to-end insights
- Cluster management: YARN manages Spark resources; ZooKeeper coordinates Kafka/HBase