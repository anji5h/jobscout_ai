FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m playwright install chromium --with-deps --only-shell

COPY . .
RUN mkdir -p /data
CMD ["celery", "-A", "app.celery_app", "worker", "--beat", "--loglevel=info"]