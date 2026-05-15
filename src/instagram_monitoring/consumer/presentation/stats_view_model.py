from dataclasses import dataclass

from instagram_monitoring import StatsSnapshot


@dataclass
class StatsViewModel:
    stats: list[StatsSnapshot]
    author: str
    stat_style: str = ""
    border_style: str = "cyan"
    title_style: str = "bold cyan"
