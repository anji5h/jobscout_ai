# ---- builder ----
FROM python:3.12-slim AS builder

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium --with-deps --no-shell

# ---- runtime ----
FROM python:3.12-slim

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /ms-playwright /ms-playwright

COPY . .

RUN useradd -m jobscoutuser && \
    mkdir -p /data && \
    chown -R jobscoutuser:jobscoutuser /app /data /ms-playwright

USER jobscoutuser

CMD ["celery", "-A", "app.celery_app", "worker", "--beat", "--loglevel=info"]