import sys
from instagram_monitoring.domain.post_published_event import InstagramAnalyticsApp
from kafka import KafkaProducer # type: ignore
from instagram_monitoring import PostPublishedEvent, config


def main():
    if len(sys.argv) < 3:
        print("\n❌ Erro: Argumentos insuficientes.")
        print("Uso: uv run seu_script.py <@usuario> <N_total> ")
        print("Exemplo: uv run main.py neymarjr 20\n")
        sys.exit(1)

    username = sys.argv[1].replace("@", "")
    try:
        n_adj = int(sys.argv[2]) 
    except ValueError:
        print("Erro: N e M devem ser números inteiros.")
        sys.exit(1)

    app = InstagramAnalyticsApp()
    
    events = app.get_events(username, n=n_adj)

    if not events:
        print(f"⚠️ Nenhum post encontrado para @{username} ou erro na API.")
        return

    print(f"📤 Enviando {len(events)} eventos para o Kafka...")
    for event in events:
        app.produce_to_kafka(event)

if __name__ == "__main__":
    main()
