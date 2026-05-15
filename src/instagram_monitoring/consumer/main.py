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
        print("\nConsumer interrupted. Exiting...")
    finally:
        consumer.close()


def consume_messages(consumer):
    stats_aggr = RollingStatsAggregator(window_len=config.STATS_WINDOW_LEN)

    for msg in consumer:
        # Extração dos dados brutos
        event = {
            "id": msg.value.get("id"),
            "views": msg.value.get("views", 0),
            "likes": msg.value.get("likes", 0),
            "comments": msg.value.get("comments", 0),
            "author": msg.value.get("author", "Unknown")
        }
        
        # Adiciona e verifica se é um post novo
        is_new = stats_aggr.add(event)
        
        if not is_new:
            continue # Pula a renderização se o post for repetido
        # Busca o histórico APENAS do autor deste post
        user_history = stats_aggr.get_history(event["author"])

        stats_viewmodel = StatsViewModel(
            history=user_history, 
            author=event["author"],
            n_window=config.STATS_WINDOW_LEN,
            m_window=1
        )

        stats_renderable = stats_widget.render(stats_viewmodel)
        terminal_display.display(stats_renderable)


if __name__ == "__main__":
    main()