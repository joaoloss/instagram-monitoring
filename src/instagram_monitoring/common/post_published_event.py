from dataclasses import dataclass


@dataclass
class PostPublishedEvent:
    post_id: str
    n_views: int
    n_likes: int
    n_comments: int
