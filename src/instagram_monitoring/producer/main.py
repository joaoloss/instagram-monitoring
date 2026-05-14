from kafka import KafkaProducer

from instagram_monitoring import config


def main():
    print("Producer is running...")

    bootstrap_servers = config.BOOTSTRAP_SERVERS
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    for _ in range(10):
        msg = b"Test message."
        print(f"Sending message: {msg.decode('utf-8')}")
        producer.send("test-topic", msg)
    producer.flush()


if __name__ == "__main__":
    main()
