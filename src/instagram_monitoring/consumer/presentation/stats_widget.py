from instagram_monitoring.consumer.presentation.stats_view_model import StatsViewModel
import numpy as np # type: ignore
from rich.align import Align # type: ignore
from rich.columns import Columns # type: ignore
from rich.panel import Panel # type: ignore
from rich.text import Text # type: ignore

def render(view_model: StatsViewModel):
    metrics_map = [("Visualizações", "views"), ("Curtidas", "likes"), ("Comentários", "comments")]
    
    texts = []
    for label, key in metrics_map:
        mean, std, total = _compute_metrics(view_model.history, key)
        
        metric_text = Text(justify="left")
        metric_text.append(f"📊 {label}\n", style=f"bold {view_model.stat_style}")
        metric_text.append(f"  Média: {mean:>10.2f}\n", style="white")
        metric_text.append(f"  Desvio: {std:>9.2f}\n", style="white")
        metric_text.append(f"  Total: {total:>10}\n", style="bold cyan")
        
        texts.append(metric_text)

    title = Text.assemble(
        (f" Monitorando @{view_model.author} ", "bold black on cyan"),
        (f" (Janela: {len(view_model.history)} posts)", "italic gray50")
    )

    columns = Columns(texts, padding=(0, 4), equal=True, expand=True)
    
    panel = Panel(
        columns,
        title=title,
        subtitle="[bold yellow]SITUAÇÕES DE INTERESSE[/] | " + _check_alerts(view_model),
        border_style=view_model.border_style,
        padding=(1, 2)
    )

    return Align.center(panel)

def _compute_metrics(history: list[dict], metric_key: str):
    values = np.array([post.get(metric_key, 0) for post in history])
    
    if values.size == 0:
        return 0.0, 0.0, 0
        
    return float(np.mean(values)), float(np.std(values)), int(np.sum(values))

def _check_alerts(vm: StatsViewModel) -> str:
    """
    Avalia o post mais recente contra o histórico total.
    Categorias: Viral, Flopado ou Estável.
    """
    if len(vm.history) < 2:
        return "Coletando dados..."
    
    likes = np.array([p.get('likes', 0) for p in vm.history])
    mu = np.mean(likes)
    sigma = np.std(likes)
    
    post_mais_recente = max(vm.history, key=lambda x: int(x['id']))
    current = post_mais_recente['likes']
    
    upper_bound = mu + 1.5 * sigma
    lower_bound = mu - 1.5 * sigma

    if current > upper_bound:
        return f"[bold green]🚀 VIRAL DETECTADO![/] ({current} likes > limiar {upper_bound:.0f})"
    
    if current < lower_bound:
        return f"[bold red]📉 QUEDA DE ENGAJAMENTO![/] ({current} likes < limiar {lower_bound:.0f})"
    
    return f"[green]✅ ESTÁVEL[/] (Dentro da média de {mu:.0f})"
    