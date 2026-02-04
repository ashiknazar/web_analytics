from kafka import KafkaProducer
import json, time, uuid, random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(1,100)}",
        "event_type": random.choice(["page_view", "click"]),
        "page_url": random.choice(["/", "/login", "/products"]),
        "event_time": datetime.utcnow().isoformat()
    }

while True:
    producer.send("web_analytics", generate_event())
    time.sleep(2)