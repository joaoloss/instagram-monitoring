from rich import print as rprint # type: ignore
from rich.console import RenderableType # type: ignore
from rich.layout import Layout # type: ignore


def display(stats_render: RenderableType) -> None:
    layout = Layout()
    layout.split_column(
        Layout(stats_render, name="stats"),
    )
    rprint(layout)
