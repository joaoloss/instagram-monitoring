FROM python:3.14-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock* README.md ./
COPY src ./src

RUN uv sync --frozen

COPY .env* ./

# To see logs in real-time
ENV PYTHONUNBUFFERED=1

# Default to producer, but can be overridden
ENTRYPOINT ["uv", "run"]
CMD ["producer"]
