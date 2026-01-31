from flask import Flask, jsonify
from kafka import KafkaProducer, errors
import json, time, random, os

app = Flask(__name__)

KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "kafka:9092")
TOPIC = "user_events"

# Retry until Kafka is ready
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        print("Kafka connected!")
        break
    except errors.NoBrokersAvailable:
        print("Kafka not ready, retrying in 2 seconds...")
        time.sleep(2)

@app.route("/produce")
def produce():
    event = {
        "user_id": random.randint(1000, 9999),
        "event": random.choice(["login", "click", "purchase", "logout"]),
        "timestamp": int(time.time())
    }

    producer.send(TOPIC, event)
    producer.flush()

    return jsonify(event)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)