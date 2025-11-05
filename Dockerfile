FROM python:3.11-slim

WORKDIR /app

COPY BackEnd/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY BackEnd/ .

CMD ["python", "-m", "pytest"]
