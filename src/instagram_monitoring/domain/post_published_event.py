import json
import os
import requests # type: ignore
from dataclasses import dataclass
from kafka import KafkaProducer # type: ignore

from instagram_monitoring import config

@dataclass
class PostPublishedEvent:
    id: str
    n_views: int
    n_likes: int
    n_comments: int
    author: str

class InstagramAnalyticsApp:
    def __init__(self):
        self.base_url = "https://instagram-looter2.p.rapidapi.com"
        self.headers = {
            "x-rapidapi-key": config.API_KEY,
            "x-rapidapi-host": "instagram-looter2.p.rapidapi.com"
        }

        try:
            self.producer = KafkaProducer(
                bootstrap_servers=config.BOOTSTRAP_SERVERS,
                value_serializer=lambda v: json.dumps(v).encode("utf-8")
            )
            print("✅ Conexão com Kafka inicializada.")
        except Exception as e:
            print(f"❌ Falha ao conectar no Kafka: {e}")
            self.producer = None

    def get_events(self, username: str, n: int = 12):
        """Coleta os dados filtrando apenas os campos necessários na API."""
        
        id_res = requests.get(
            f"{self.base_url}/id", 
            params={"username": username, "fields": "user_id"}, 
            headers=self.headers
        ).json()
        user_id = id_res.get("user_id") 
        if not user_id: 
            print(f"⚠️ Usuário {username} não encontrado.")
            return []

        print(f"🔎 Coletando os últimos {n} posts de @{username} (id {user_id})...")

        query_fields = "items[].pk,items[].play_count,items[].like_count,items[].comment_count,items[].user.username,"

        feed_res = requests.get(
            f"{self.base_url}/user-feeds", 
            params={
                "id": user_id, 
                "count": n,
                "fields": query_fields 
            }, 
            headers=self.headers
        ).json()
        items = feed_res.get("items", [])
        
        posts_events = []
        for item in items:
            event = PostPublishedEvent(
                id=str(item.get("pk")),
                n_views=item.get("play_count", 0), 
                n_likes=item.get("like_count", 0),
                n_comments=item.get("comment_count", 0),
                author=item.get("user", {}).get("username", username)
            )
            posts_events.append(event)
            
        return posts_events
    
    def produce_to_kafka(self, event: PostPublishedEvent):
        """Envia o evento para o tópico 'post-stats' formatado como JSON."""
        
        payload = {
            "id": event.id,
            "views": event.n_views,
            "likes": event.n_likes,
            "comments": event.n_comments,
            "author": event.author
        }

        try:
            future = self.producer.send(config.TOPIC, value=payload)
            
            record_metadata = future.get(timeout=10)
            
            print(f"✅ [KAFKA] Mensagem enviada: {event.id} | Partição: {record_metadata.partition} | Offset: {record_metadata.offset}")
            
        except Exception as e:
            print(f"❌ [KAFKA] Erro ao enviar evento {event.id}: {e}")

    def close(self):
        """Garante que todas as mensagens pendentes sejam enviadas antes de fechar."""
        self.producer.flush()
        self.producer.close()
