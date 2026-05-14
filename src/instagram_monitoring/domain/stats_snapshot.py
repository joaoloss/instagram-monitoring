from dataclasses import dataclass


@dataclass(frozen=True)
class StatsSnapshot:
    mean_views: float
    std_views: float
    total_views: int
