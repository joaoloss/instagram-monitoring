from instagram_monitoring.consumer.presentation.stats_view_model import StatsViewModel
import numpy as np # type: ignore
from rich.align import Align # type: ignore
from rich.columns import Columns # type: ignore
from rich.panel import Panel # type: ignore
from rich.text import Text # type: ignore

def render(view_model: StatsViewModel):
    # Métricas que queremos monitorar (mapeadas para as chaves do JSON do Kafka)
    metrics_map = [("Visualizações", "views"), ("Curtidas", "likes"), ("Comentários", "comments")]
    
    texts = []
    for label, key in metrics_map:
        mean, std, total = _compute_metrics(view_model.history, key)
        
        # Criando o bloco de texto para cada métrica
        metric_text = Text(justify="left")
        metric_text.append(f"📊 {label}\n", style=f"bold {view_model.stat_style}")
        metric_text.append(f"  Média: {mean:>10.2f}\n", style="white")
        metric_text.append(f"  Desvio: {std:>9.2f}\n", style="white")
        metric_text.append(f"  Total: {total:>10}\n", style="bold cyan")
        
        texts.append(metric_text)

    # Título do Painel
    title = Text.assemble(
        (f" Monitorando @{view_model.author} ", "bold black on cyan"),
        (f" (Janela: {len(view_model.history)} posts)", "italic gray50")
    )

    # Organização em colunas
    columns = Columns(texts, padding=(0, 4), equal=True, expand=True)
    
    # Criamos o painel principal
    panel = Panel(
        columns,
        title=title,
        subtitle="[bold yellow]SITUAÇÕES DE INTERESSE[/] | " + _check_alerts(view_model),
        border_style=view_model.border_style,
        padding=(1, 2)
    )

    return Align.center(panel)

def _compute_metrics(history: list[dict], metric_key: str):
    # Extrai apenas os valores da métrica específica
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
    
    # 1. Pega os likes de todo o histórico para criar a régua estatística
    likes = np.array([p.get('likes', 0) for p in vm.history])
    mu = np.mean(likes)      # Média histórica
    sigma = np.std(likes)    # Volatilidade histórica
    
    # 2. Pega apenas o post mais recente (o atual)
    # 1. Localiza o dicionário que tem o ID numérico mais alto
    post_mais_recente = max(vm.history, key=lambda x: int(x['id']))
    # 2. Extrai o valor de likes desse dicionário
    current = post_mais_recente['likes']
    
    # Definimos os limites baseados no desvio padrão
    # 1.5 é um multiplicador comum, mas você pode ajustar
    upper_bound = mu + 1.5 * sigma
    lower_bound = mu - 1.5 * sigma

    print(likes[0], lower_bound, upper_bound)
    
    # 3. Classificação
    if current > upper_bound:
        return f"[bold green]🚀 VIRAL DETECTADO![/] ({current} likes > limiar {upper_bound:.0f})"
    
    if current < lower_bound:
        return f"[bold red]📉 QUEDA DE ENGAJAMENTO![/] ({current} likes < limiar {lower_bound:.0f})"
    
    return f"[green]✅ ESTÁVEL[/] (Dentro da média de {mu:.0f})"
    