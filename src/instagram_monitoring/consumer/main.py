import json

from kafka import KafkaConsumer

from instagram_monitoring import PostPublishedEvent, config


def main():
    print("Consumer is running...")

    consumer = KafkaConsumer(
        config.TOPIC,
        bootstrap_servers=config.BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
        group_id="test-group",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )

    try:
        for message in consumer:
            event = PostPublishedEvent(**message.value)
            print(f"Received event: {event}")
    except KeyboardInterrupt:
        print("Consumer interrupted. Exiting...")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
