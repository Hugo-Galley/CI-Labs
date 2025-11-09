FROM python:3.11-slim

WORKDIR /app

COPY BackEnd/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY BackEnd/ .

LABEL org.opencontainers.image.title="Ci-Labs" \
      org.opencontainers.image.description="A test description" \
      org.opencontainers.image.url="https://galleyhugo.com" \
      org.opencontainers.image.source="https://github.com/Hugo-Galley/Ci-Labs" \
      org.opencontainers.image.licenses="MIT"

CMD ["python", "-m", "pytest"]
