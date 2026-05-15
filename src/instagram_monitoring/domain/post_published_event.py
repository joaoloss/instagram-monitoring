from dataclasses import dataclass


@dataclass
class PostPublishedEvent:
    id: str
    n_views: int
    n_likes: int
    n_comments: int
    author: str
