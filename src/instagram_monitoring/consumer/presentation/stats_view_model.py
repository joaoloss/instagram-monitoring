from dataclasses import dataclass, field

@dataclass
class StatsViewModel:
    history: list[dict] = field(default_factory=list)
    author: str = "Unknown"
    n_window: int = 20
    m_window: int = 5
    title_style: str = "bold white"
    border_style: str = "cyan"
    stat_style: str = "green"