#### 1. Real-Life Problem Being Solved
- Modern web applications need to monitor user activity in real time to understand:
  - How many users are active
  - What actions users perform
  - Whether errors or performance issues are occurring
___
#### 2. Data Source (Very Clear)
Data Source Design
- 3 Flask applications
- Each Flask app simulates 10 concurrent users
- Each user generates webpage activity events continuously
___
#### 3. Event Data (What Is Being Streamed)

```json
{
  "app_id": "flask_app_1",
  "user_id": 4,
  "session_id": "fa1_sess_4",
  "page": "/products",
  "action": "click",
  "response_time_ms": 240,
  "status": "success",
  "timestamp": "2026-01-16T18:10:12"
}

```
___
#### 4. Complete Tool Stack (All Major Big Data Tools)
- Data Generation
  - Flask (3 instances)
- Streaming & Ingestion
  - Apache Kafka
  - ZooKeeper / KRaft
- Distributed Storage
  - HDFS
- Processing Engine
  - Apache Spark
- Resource Management
  - YARN
- Query & Analytics
  - Apache Hive
- Orchestration
  - Apache Airflow
- Visualization
  - Streamlit
- Containerization
  - Docker & Docker Compose
___
#### 5. Full System Architecture
```
[Flask App 1] \
[Flask App 2]  -->  Kafka  -->  Spark Streaming  -->  HDFS
[Flask App 3] /                         |
                                        |
                                  Spark Batch
                                        |
                                      Hive
                                        |
                                   Streamlit

Airflow --> Spark / Hive Jobs
YARN --> Resource Management
ZooKeeper --> Coordination
```
___
#### 6. Abstract
> This project presents the design and implementation of an end-to-end Big Data analytics platform for real-time user activity monitoring using a Docker-based pseudo-distributed cluster. The system simulates realistic web application behavior through multiple Flask applications, each generating continuous streams of user interaction events from concurrent users. These events represent typical webpage activities such as page views, clicks, and form submissions.
>
> Apache Kafka is used as the streaming ingestion layer to handle high-velocity event data, while Apache Spark processes the data using both structured streaming and batch analytics paradigms. Distributed storage is provided by HDFS, enabling scalable and fault-aware persistence of raw and processed user activity data. Resource allocation and job scheduling are managed through YARN, simulating multi-node cluster execution.
>
> Higher-level analytics are performed using Hive, allowing SQL-based querying over large volumes of historical user activity data. Workflow orchestration is handled using Apache Airflow, and analytical insights are visualized through a Streamlit-based dashboard. All components are deployed as independent Docker containers, effectively emulating a multi-node Big Data cluster on a single physical machine.
The project emphasizes architectural design, system integration, and practical understanding of Big Data ecosystem tools rather than production-scale performance. It demonstrates how real-time and batch analytics can be implemented for user activity monitoring in modern data-driven web systems.
___
