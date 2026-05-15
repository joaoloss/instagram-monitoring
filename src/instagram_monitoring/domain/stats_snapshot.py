from dataclasses import dataclass


@dataclass(frozen=True)
class StatsSnapshot:
    mean_views: float
    std_views: float
    total_views: int

    mean_likes: float
    std_likes: float
    total_likes: int

    mean_comments: float
    std_comments: float
    total_comments: int
