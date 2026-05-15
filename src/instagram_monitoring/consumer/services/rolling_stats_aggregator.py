from collections import deque

import numpy as np

from instagram_monitoring import PostPublishedEvent, StatsSnapshot


class RollingStatsAggregator:
    def __init__(self, window_len: int) -> None:
        self._posts: deque[PostPublishedEvent] = deque(maxlen=window_len)

    def add(self, post: PostPublishedEvent):
        self._posts.append(post)

    def compute_stats(self) -> StatsSnapshot:
        views = np.array([post.n_views for post in self._posts])
        likes = np.array([post.n_likes for post in self._posts])
        comments = np.array([post.n_comments for post in self._posts])

        return StatsSnapshot(
            mean_views=views.mean(),
            std_views=views.std(),
            total_views=views.sum(),
            mean_likes=likes.mean(),
            std_likes=likes.std(),
            total_likes=likes.sum(),
            mean_comments=comments.mean(),
            std_comments=comments.std(),
            total_comments=comments.sum(),
        )

    def clear(self):
        self._posts.clear()

    @property
    def posts(self) -> list[PostPublishedEvent]:
        return list(self._posts)
