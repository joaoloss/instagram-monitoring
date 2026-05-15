class RollingStatsAggregator:
    def __init__(self, window_len: int):
        self.window_len = window_len
        self.history_by_user = {} 
        self.seen_ids = set()

    def add(self, event: dict):
        post_id = event.get("id")
        author = event.get("author")

        if post_id in self.seen_ids:
            return False
        
        self.seen_ids.add(post_id)

        if author not in self.history_by_user:
            self.history_by_user[author] = []

        user_posts = self.history_by_user[author]
        user_posts.append(event)

        if len(user_posts) > self.window_len:
            removed = user_posts.pop(0)
            self.seen_ids.remove(removed.get("id"))
            
        return True

    def get_history(self, author: str):
        return self.history_by_user.get(author, [])