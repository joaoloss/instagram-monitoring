from instagram_monitoring import PostPublishedEvent, StatsSnapshot, config
from instagram_monitoring.consumer.infra.post_consumer import PostConsumer
from instagram_monitoring.consumer.presentation import stats_widget, terminal_display
from instagram_monitoring.consumer.presentation.stats_view_model import StatsViewModel


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
        event = PostPublishedEvent(
            id=msg.value["id"],
            n_views=msg.value["n_views"],
            n_likes=msg.value["n_likes"],
            n_comments=msg.value["n_comments"],
            author=msg.value["author"],
        )
        stats = StatsSnapshot(
            mean_views=event.n_views,
            std_views=0.0,
            total_views=event.n_views,
            mean_likes=1.0,
            std_likes=2.0,
            total_likes=3,
            mean_comments=1.0,
            std_comments=2.0,
            total_comments=3,
        )
        stats_viewmodel = StatsViewModel(stats=[stats], author=event.author)
        stats_renderable = stats_widget.render(stats_viewmodel)
        terminal_display.display(stats_renderable)


if __name__ == "__main__":
    main()
