import os

API_KEY = os.getenv("RAPIDAPI_KEY", "your_rapidapi_key_here")
BOOTSTRAP_SERVERS = os.getenv(
    "BOOTSTRAP_SERVERS", "localhost:29092,localhost:39092,localhost:49092"
)
TOPIC = "post-stats"

STATS_WINDOW_LEN = 30
