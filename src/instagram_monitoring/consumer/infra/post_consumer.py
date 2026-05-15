import json

from kafka import KafkaConsumer # type: ignore

from instagram_monitoring import PostPublishedEvent


class PostConsumer:
    def __init__(self, topic: str, bootstrap_servers: str, group_id: str):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset="earliest",
            group_id=group_id,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )

    def __iter__(self):
        return self.consumer

    def __next__(self):
        msg = next(self.consumer)
        return PostPublishedEvent(**msg.value)

    def close(self):
        self.consumer.close()
