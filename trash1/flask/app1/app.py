from flask import Flask
import json, time, random, datetime
from kafka import KafkaProducer

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

PAGES = ["/home", "/products", "/cart", "/checkout"]
SECTIONS = ["header", "product_list", "footer"]

@app.route("/generate")
def generate():
    for user_id in range(1, 11):
        event = {
            "app_id": "flask_app_1",
            "user_id": user_id,
            "session_id": f"sess_{user_id}",
            "page": random.choice(PAGES),
            "section": random.choice(SECTIONS),
            "event_type": random.choice(["click", "scroll", "view"]),
            "country": "India",
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
        producer.send("user_events", event)
    return "Events sent"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
