import numpy as np
from rich.align import Align
from rich.columns import Columns
from rich.console import RenderableType
from rich.panel import Panel
from rich.text import Text

from instagram_monitoring import StatsSnapshot
from instagram_monitoring.consumer.presentation.stats_view_model import StatsViewModel


def render(view_model: StatsViewModel) -> RenderableType:
    metrics = [("Views", "views"), ("Likes", "likes"), ("Comments", "comments")]

    texts = []
    for label, metric in metrics:
        mean, std, total = _compute_metrics(view_model.stats, metric)
        text = _build_metric_text(
            label=label,
            mean=mean,
            std=std,
            total=total,
            stat_style=view_model.stat_style,
        )
        texts.append(text)

    title = Text.assemble(
        (f"Last {len(view_model.stats)} posts from "),
        (view_model.author, "u"),
        style=view_model.title_style,
    )

    columns = Columns(texts, padding=(0, 4), equal=True, expand=True, align="center")
    panel = Panel(
        columns,
        title=title,
        border_style=view_model.border_style,
        padding=(1, 2),
        expand=False,
    )

    return Align.center(panel, vertical="middle")


def _build_metric_text(
    label: str, mean: float, std: float, total: int, stat_style: str
) -> Text:
    mean_label = f"Mean {label}: "
    std_label = f"Std {label}: "
    total_label = f"Total {label}: "

    mean_stat = f"{mean:.2f}\n"
    std_stat = f"{std:.2f}\n"
    total_stat = f"{total}\n"

    label_style = stat_style
    stats_style = "bold " + stat_style

    return Text.assemble(
        (mean_label, label_style),
        (mean_stat, stats_style),
        (std_label, label_style),
        (std_stat, stats_style),
        (total_label, label_style),
        (total_stat, stats_style),
        justify="left",
    )


def _compute_metrics(
    snapshots: list[StatsSnapshot],
    metric: str,
) -> tuple[float, float, int]:
    means = np.array([getattr(stat, f"mean_{metric}") for stat in snapshots])
    stds = np.array([getattr(stat, f"std_{metric}") for stat in snapshots])
    totals = np.array([getattr(stat, f"total_{metric}") for stat in snapshots])

    mean = np.mean(means) if means.size > 0 else np.nan
    std = np.mean(stds) if stds.size > 0 else np.nan
    total = np.sum(totals) if totals.size > 0 else 0

    return float(mean), float(std), total
