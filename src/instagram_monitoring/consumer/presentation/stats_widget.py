import numpy as np
from rich.align import Align
from rich.console import RenderableType
from rich.panel import Panel
from rich.text import Text

from instagram_monitoring import StatsSnapshot


def render(stats: list[StatsSnapshot]) -> RenderableType:
    means = np.array([s.mean_views for s in stats])
    stds = np.array([s.std_views for s in stats])
    totals = np.array([s.total_views for s in stats])

    mean_views = np.mean(means) if means.size > 0 else np.nan
    stds_views = np.mean(stds) if stds.size > 0 else np.nan
    total_views = np.sum(totals) if totals.size > 0 else 0

    text = Text.assemble(
        ("Mean Views: "),
        (f"{mean_views:.2f}\n", "bold"),
        ("Std Views: "),
        (f"{stds_views:.2f}\n", "bold"),
        ("Total Views: "),
        (f"{total_views}\n", "bold"),
        justify="center",
    )

    panel = Panel(
        text, title="[bold]Post Statistics[/]", border_style="cyan", padding=(1, 2)
    )

    return Align.center(panel, vertical="middle")
