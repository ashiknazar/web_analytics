from kafka import KafkaConsumer
import json
from datetime import datetime
from hdfs import InsecureClient

consumer = KafkaConsumer(
    "web_analytics",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="hdfs-writer"
)

hdfs = InsecureClient("http://hdfs-namenode:50070", user="root")

buffer = []
BATCH_SIZE = 10

for msg in consumer:
    buffer.append(msg.value)

    if len(buffer) >= BATCH_SIZE:
        date = datetime.utcnow().strftime("%Y-%m-%d")
        ts = datetime.utcnow().strftime("%H%M%S")
        hdfs_path = f"/data/raw/web_analytics/dt={date}/events_{ts}.json"

        hdfs.makedirs(f"/data/raw/web_analytics/dt={date}", permission=777)

        with hdfs.write(hdfs_path, encoding="utf-8") as f:
            for event in buffer:
                f.write(json.dumps(event) + "\n")

        print(f"Wrote {len(buffer)} events → {hdfs_path}")
        buffer.clear()
