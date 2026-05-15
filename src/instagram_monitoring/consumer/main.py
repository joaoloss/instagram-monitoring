from instagram_monitoring import PostPublishedEvent, config
from instagram_monitoring.consumer.infra.post_consumer import PostConsumer
from instagram_monitoring.consumer.presentation import stats_widget, terminal_display
from instagram_monitoring.consumer.presentation.stats_view_model import StatsViewModel
from instagram_monitoring.consumer.services.rolling_stats_aggregator import (
    RollingStatsAggregator,
)


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
    stats_aggr = RollingStatsAggregator(window_len=config.STATS_WINDOW_LEN)
    posts_history = []

    for msg in consumer:
        event = PostPublishedEvent(
            id=msg.value["id"],
            n_views=msg.value["n_views"],
            n_likes=msg.value["n_likes"],
            n_comments=msg.value["n_comments"],
            author=msg.value["author"],
        )

        stats_aggr.add(event)
        posts_history.append(stats_aggr.compute_stats())

        stats_viewmodel = StatsViewModel(history=posts_history, author=event.author)
        stats_renderable = stats_widget.render(stats_viewmodel)
        terminal_display.display(stats_renderable)


if __name__ == "__main__":
    main()
