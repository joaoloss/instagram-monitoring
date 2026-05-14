from instagram_monitoring import PostPublishedEvent, StatsSnapshot, config
from instagram_monitoring.consumer.infra.post_consumer import PostConsumer
from instagram_monitoring.consumer.presentation import stats_widget, terminal_display


def main():
    print("Consumer is running...")

    consumer = PostConsumer(
        config.TOPIC,
        bootstrap_servers=config.BOOTSTRAP_SERVERS,
        group_id="test-group",
    )

    try:
        consume_messages(consumer)
    except KeyboardInterrupt:
        print("Consumer interrupted. Exiting...")
    finally:
        consumer.close()


def consume_messages(consumer):
    for msg in consumer:
        event = PostPublishedEvent(**msg.value)
        stats = StatsSnapshot(
            mean_views=event.n_views,
            std_views=0.0,
            total_views=event.n_views,
        )

        stats_renderable = stats_widget.render([stats])
        terminal_display.display(stats_renderable)


if __name__ == "__main__":
    main()
