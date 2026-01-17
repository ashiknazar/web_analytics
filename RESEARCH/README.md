# Tool-wise Implementation Plan

This document describes **what is implemented using each Big Data tool** in this project.  
The goal is to clearly map **project functionality → tool responsibility**, ensuring conceptual clarity and avoiding ambiguity.

---

## 1. Flask (Data Generation Layer)

### What Will Be Implemented

- Three independent Flask applications
- Each Flask app simulates:
  - 10 concurrent users
  - Continuous generation of user activity events

### Responsibilities

- Mimic real-world web user behavior
- Generate synthetic but realistic events such as:
  - Page navigation
  - Button clicks
  - Section-level interactions
  - Session-based user activity
- Push events to Kafka topics using a Kafka producer

### Why Flask Is Used

- Lightweight
- Easy to simulate HTTP-based user activity
- Ideal for synthetic streaming data generation

---

## 2. Apache Kafka (Streaming & Ingestion Layer)

### What Will Be Implemented

- Kafka cluster running in Docker
- One or more Kafka topics for user activity events
- Kafka producers in Flask apps
- Kafka consumers in Spark Streaming

### Responsibilities

- Act as a high-throughput event ingestion system
- Buffer incoming user activity streams
- Decouple data producers (Flask) from consumers (Spark)

### Why Kafka Is Used

- Industry standard for real-time streaming
- Handles high-velocity, continuous event data
- Supports scalable, fault-tolerant ingestion

---

## 3. ZooKeeper / KRaft (Cluster Coordination)

### What Will Be Implemented

- Kafka coordination and metadata management
- Broker registration and leader election

### Responsibilities

- Maintain Kafka cluster state
- Ensure reliable coordination between Kafka components

### Why It Is Used

- Required for Kafka cluster management
- Demonstrates distributed system coordination concepts

---

## 4. Apache Spark Structured Streaming (Real-Time Processing)

### What Will Be Implemented

- Spark Structured Streaming jobs consuming Kafka topics
- Real-time transformations such as:
  - Active user counts
  - Page visit frequency
  - Section-level interaction metrics
  - Average time spent per page
  - Navigation path analysis (previous → current → next)

### Responsibilities

- Process streaming data in near real time
- Perform aggregations and window-based analytics
- Write processed results to HDFS

### Why Spark Streaming Is Used

- Unified engine for batch and streaming
- Scales across multiple nodes
- Widely used in enterprise Big Data systems

---

## 5. HDFS (Distributed Storage Layer)

### What Will Be Implemented

- HDFS pseudo-distributed cluster using Docker
- Storage of:
  - Raw streaming events
  - Processed streaming outputs
  - Historical batch data

### Responsibilities

- Provide fault-tolerant distributed storage
- Act as the system of record for analytics

### Why HDFS Is Used

- Core storage layer in Hadoop ecosystem
- Enables large-scale batch analytics
- Demonstrates distributed file system concepts

---

## 6. Apache Spark Batch Processing

### What Will Be Implemented

- Batch jobs reading historical data from HDFS
- Analytical computations such as:
  - Most visited pages
  - Most interacted sections
  - User navigation funnels
  - Geographic user distribution
  - Peak activity times

### Responsibilities

- Perform deep historical analysis
- Prepare datasets for reporting and visualization

### Why Spark Batch Is Used

- Efficient large-scale data processing
- Same engine as streaming (simplifies architecture)

---

## 7. Apache Hive (SQL Analytics Layer)

### What Will Be Implemented

- Hive external tables over HDFS data
- SQL queries for:
  - Page-level analytics
  - Section engagement analysis
  - Session-based metrics
  - Performance monitoring queries

### Responsibilities

- Enable SQL-based analytics
- Provide analyst-friendly access to data

### Why Hive Is Used

- Familiar SQL interface
- Common in enterprise data warehouses
- Bridges Big Data storage and analytics users

---

## 8. YARN (Resource Management)

### What Will Be Implemented

- YARN-based resource scheduling for Spark jobs
- Multi-container execution simulation

### Responsibilities

- Allocate CPU and memory resources
- Manage execution of Spark jobs across nodes

### Why YARN Is Used

- Core Hadoop resource manager
- Demonstrates cluster-level job scheduling

---

## 9. Apache Airflow (Workflow Orchestration)

### What Will Be Implemented

- DAGs to orchestrate:
  - Spark streaming startup
  - Scheduled Spark batch jobs
  - Hive query execution

### Responsibilities

- Automate data pipelines
- Manage task dependencies
- Schedule recurring analytics workflows

### Why Airflow Is Used

- Industry-standard orchestration tool
- Clear visualization of data pipelines

---

## 10. Streamlit (Visualization Layer)

### What Will Be Implemented

- Dashboards showing:
  - Active users
  - Most visited pages
  - Section-level engagement
  - Navigation flows
  - Geographic distribution

### Responsibilities

- Visualize real-time and historical analytics
- Provide an interactive analytics interface

### Why Streamlit Is Used

- Fast dashboard development
- Python-native visualization
- Ideal for analytical prototypes

---

## 11. Docker & Docker Compose (Deployment Layer)

### What Will Be Implemented

- Docker containers for all components
- Docker Compose to define multi-service setup
- Simulated multi-node cluster on a single machine

### Responsibilities

- Isolate services
- Enable reproducible deployments
- Emulate a distributed Big Data cluster

### Why Docker Is Used

- No need for physical multi-node hardware
- Simplifies complex Big Data deployments
- Industry-relevant deployment skill

---

## Summary

This project focuses on **understanding how Big Data systems are designed, integrated, and operated** by implementing a realistic end-to-end analytics platform using containerized multi-node clustering.  
The emphasis is on **architecture, tool interaction, and data flow**, rather than raw data volume.
