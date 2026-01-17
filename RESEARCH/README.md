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
____

<img src="../images/logo.png" style="width:100vw; height:100vh; object-fit:contain;">
__


# Project Implementation & Expected Results

This document explains **what is actually implemented in this project**, how data flows through the system, and **what analytical results are produced** using each Big Data tool.

The project simulates a real-world **user activity monitoring system** for a web application.

---

## 1. What This Project Simulates

This project simulates:

- Users visiting a website
- Users navigating between pages
- Users interacting with specific sections of pages
- Users coming from different locations and referrers
- The system collecting and analyzing this behavior in real time

There is **no external data source**.  
All data is **synthetically generated** but **realistic**.

---

## 2. Data Generation (Flask Applications)

### What You Will Implement

- Three Flask applications running simultaneously
- Each Flask app simulates 10 users
- Total simulated users at any moment: **30 users**
- Each user continuously generates activity events

### What Data Is Generated

Each user event represents:

- A page visit or interaction
- Movement from one page to another
- Interaction with a specific section of the page
- Time spent on the page
- Response time of the application
- User location and referrer source

### Result Produced

- Continuous stream of structured user activity events
- Events are sent to Kafka topics in real time

---

## 3. Streaming Ingestion (Kafka)

### What You Will Implement

- Kafka topics for user activity events
- Flask apps act as Kafka producers
- Spark Streaming acts as Kafka consumer

### What Kafka Does With the Data

- Buffers incoming user events
- Ensures events are not lost
- Allows multiple consumers to read the same stream

### Result Produced

- Ordered, fault-tolerant stream of user activity data
- Decoupling between data generation and processing

---

## 4. Real-Time Processing (Spark Structured Streaming)

### What You Will Implement

Spark Streaming jobs that compute real-time metrics such as:

- Number of active users per page
- Most visited pages in the last time window
- Most interacted page sections
- Average time spent per page
- Navigation flow between pages

### Example Real-Time Results

- “/products page currently has 12 active users”
- “Top section right now: product_list”
- “Average time on /checkout page: 18 seconds”
- “Most common navigation: /home → /products”

### Result Produced

- Aggregated streaming results
- Near real-time insights
- Processed data written to HDFS

---

## 5. Distributed Storage (HDFS)

### What You Will Implement

- HDFS stores:
  - Raw user activity events
  - Processed streaming outputs
  - Aggregated batch data

### What Data Looks Like in Storage

- Time-partitioned user events
- Daily/hourly aggregated analytics
- Structured datasets readable by Spark and Hive

### Result Produced

- Central historical data repository
- Fault-tolerant storage for analytics

---

## 6. Batch Analytics (Spark Batch)

### What You Will Implement

Batch jobs that analyze historical data to answer questions like:

- Which page is most visited overall?
- Which page section gets the most interaction?
- How long do users stay on each page?
- Which locations generate the most traffic?
- What are the most common user navigation paths?

### Example Batch Results

- Most visited page: /products
- Most engaged section: recommendation_grid
- Average session duration: 2.4 minutes
- Highest traffic city: Bangalore
- Most common flow: /home → /products → /checkout

### Result Produced

- Deep historical insights
- Aggregated datasets for reporting

---

## 7. SQL Analytics (Hive)

### What You Will Implement

- Hive tables on top of HDFS data
- SQL queries for analytical reporting

### Example Questions Answered Using Hive

- Page-wise user count per day
- Section-wise interaction frequency
- Session-level user behavior
- Performance error rates

### Example Results

- “/products page accounts for 38% of total traffic”
- “Add-to-cart button clicked 4,320 times”
- “Average response time increased during peak hours”

---

## 8. Workflow Automation (Airflow)

### What You Will Implement

- Airflow DAGs that:
  - Schedule batch Spark jobs
  - Trigger Hive queries
  - Manage dependencies between tasks

### Result Produced

- Automated analytics pipeline
- No manual execution needed
- Repeatable and reliable workflows

---

## 9. Visualization (Streamlit)

### What You Will Implement

Dashboards displaying:

- Live active users
- Top pages and sections
- Navigation flows
- Geographic distribution of users
- Performance metrics

### Example Visual Outputs

- Line chart of active users over time
- Bar chart of most visited pages
- Heatmap of page section engagement
- Table of navigation paths
- Map showing user locations

### Result Produced

- Interactive analytics UI
- Real-time and historical insights

---

## 10. Resource Management (YARN)

### What You Will Implement

- Spark jobs running under YARN
- Resource allocation simulation

### Result Produced

- Demonstration of multi-node scheduling
- Practical understanding of cluster execution

---

## 11. Containerized Deployment (Docker)

### What You Will Implement

- Docker containers for:
  - Flask apps
  - Kafka
  - Spark
  - HDFS
  - Hive
  - Airflow
  - Streamlit
- Docker Compose to run everything together

### Result Produced

- Pseudo-distributed Big Data cluster
- Entire system runs on one machine
- Realistic multi-node behavior

---

## Final Outcome of the Project

By the end of this project, you will have:

- A working real-time streaming pipeline
- A batch analytics system
- SQL-based analytical reporting
- Interactive dashboards
- A complete Big Data ecosystem running in Docker
- Clear understanding of how real-world Big Data systems work end-to-end
