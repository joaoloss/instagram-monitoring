import json

from kafka import KafkaProducer

from instagram_monitoring import PostPublishedEvent, config


def main():
    print("Producer is running...")

    bootstrap_servers = config.BOOTSTRAP_SERVERS
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    for _ in range(10):
        event = PostPublishedEvent(
            id="1234567890", n_views=100, n_likes=50, n_comments=10
        )
        producer.send(config.TOPIC, value=event.__dict__)
        print(f"Sent event: {event}")
    producer.flush()


if __name__ == "__main__":
    main()
