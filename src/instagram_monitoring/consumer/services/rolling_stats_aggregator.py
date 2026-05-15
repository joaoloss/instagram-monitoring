class RollingStatsAggregator:
    def __init__(self, window_len: int):
        self.window_len = window_len
        # Dicionário onde a chave é o @usuario e o valor é a lista de posts
        self.history_by_user = {} 
        # Conjunto para rastrear IDs globais e evitar duplicatas
        self.seen_ids = set()

    def add(self, event: dict):
        post_id = event.get("id")
        author = event.get("author")

        # 1. Checagem de Unicidade
        if post_id in self.seen_ids:
            return False # Ignora o post se já foi processado
        
        self.seen_ids.add(post_id)

        # 2. Separação por Usuário
        if author not in self.history_by_user:
            self.history_by_user[author] = []

        user_posts = self.history_by_user[author]
        user_posts.append(event)

        # 3. Mantém a janela N apenas para esse usuário
        if len(user_posts) > self.window_len:
            removed = user_posts.pop(0)
            self.seen_ids.remove(removed.get("id"))
            
        return True

    def get_history(self, author: str):
        return self.history_by_user.get(author, [])