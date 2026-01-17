# Real-Time User Activity Monitoring Big Data Platform

## 1. Real-Life Problem Being Solved

Modern web applications need to monitor user activity in real time to understand:

- How many users are active
- What actions users perform
- Whether errors or performance issues are occurring

This project simulates a realistic scenario to study **user behavior analytics**, **system performance**, and **stream processing**.

---

## 2. Data Source

### Data Source Design

- 3 Flask applications running concurrently
- Each Flask app simulates 10 concurrent users
- Each user generates webpage activity events continuously

These Flask applications act as **synthetic data producers**, mimicking real-world user interactions.

---

## 3. Event Data (Streamed Schema)

Each event represents **one user interaction** on a webpage.  

The schema includes:

- User information (user ID, session ID, logged-in status)
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
- Interaction performance metrics (response time, success/failure)
- Time spent on each page or section
## Sample User Activity Event (JSON)

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
---

## 4. Complete Tool Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Data Generation | Flask (3 instances) | Simulate concurrent web users and interactions |
| Streaming & Ingestion | Apache Kafka | Ingest and buffer continuous event streams |
| Coordination | ZooKeeper / KRaft | Kafka cluster metadata management |
| Distributed Storage | HDFS | Scalable and fault-tolerant storage of raw and processed events |
| Processing Engine | Apache Spark | Batch and structured streaming analytics |
| Resource Management | YARN | Multi-node cluster resource scheduling |
| Query & Analytics | Apache Hive | SQL-based querying on historical data |
| Orchestration | Apache Airflow | Pipeline scheduling and workflow management |
| Visualization | Streamlit | Real-time and historical dashboards |
| Containerization | Docker & Docker Compose | Simulate a multi-node cluster on a single machine |

---

## 5. Full System Architecture

The system architecture includes:

- Multiple Flask apps generating streaming events
- Apache Kafka for streaming ingestion
- Spark Streaming for real-time processing
- HDFS for distributed storage
- Spark Batch and Hive for batch analytics
- Streamlit dashboards for visualization
- Airflow for workflow orchestration
- YARN for resource management
- ZooKeeper for cluster coordination

---

## 6. Project Abstract

This project presents the design and implementation of an **end-to-end Big Data analytics platform** for real-time user activity monitoring using a **Docker-based pseudo-distributed cluster**.  

The system simulates realistic web application behavior through multiple Flask applications, each generating continuous streams of user interaction events from concurrent users. These events represent typical webpage activities such as page views, clicks, and form submissions.

**Apache Kafka** is used as the streaming ingestion layer to handle high-velocity event data, while **Apache Spark** processes the data using both **structured streaming** and **batch analytics** paradigms. **HDFS** provides distributed storage for scalable and fault-tolerant persistence of raw and processed user activity data. **YARN** manages resource allocation and job scheduling, simulating multi-node cluster execution.

Higher-level analytics are performed using **Hive**, allowing SQL-based querying over large volumes of historical user activity data. **Apache Airflow** handles workflow orchestration, and analytical insights are visualized through a **Streamlit** dashboard. All components are deployed as independent **Docker containers**, effectively emulating a multi-node Big Data cluster on a single physical machine.

The project emphasizes **architectural design**, **system integration**, and **practical understanding of Big Data ecosystem tools**, rather than production-scale performance. It demonstrates how **real-time and batch analytics** can be implemented for user activity monitoring in modern data-driven web systems.
