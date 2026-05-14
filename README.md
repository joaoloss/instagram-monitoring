# Instagram Monitoring

Monitors Instagram accounts for new events.

## Requirements

- Docker + Docker Compose

## How to Run

```sh
cp .env.example .env # Edit .env with your credentials
docker compose up --build
```

## Local Development

1. Create a virtual environment and activate it:

```sh
uv sync
```

1. Start the brokers:

```sh
docker compose up -d broker-1 broker-2 broker-3
```

1. Run the producer and consumer in separate terminals:

```sh
uv run producer
```

```sh
uv run consumer
```
