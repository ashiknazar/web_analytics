# Real-Time User Activity Monitoring Big Data Platform (Extended)
<!-- Original image reduced by half -->
<p align="center">
  <img src="images/logo.png" alt="Logo" width="50%" />
</p>

### Directory structure

web_analytics/
│
├── flask-app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── kafka/
│   └── (uses official image)
│
├── hdfs/
│   ├── namenode/
│   ├── datanode1/
│   └── datanode2/
│
├── spark/
│   └── (later)
│
└── docker-compose.yml