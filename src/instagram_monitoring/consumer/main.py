from kafka import KafkaConsumer

from instagram_monitoring import config


def main():
    print("Consumer is running...")

    consumer = KafkaConsumer(
        "test-topic",
        bootstrap_servers=config.BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
        group_id="test-group",
    )

    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")
    consumer.close()


if __name__ == "__main__":
    main()
