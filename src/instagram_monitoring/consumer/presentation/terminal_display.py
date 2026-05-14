from rich import print as rprint
from rich.console import RenderableType
from rich.layout import Layout


def display(stats_render: RenderableType) -> None:
    layout = Layout()
    layout.split_column(
        Layout(stats_render, name="stats"),
    )
    rprint(layout)
