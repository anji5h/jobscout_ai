FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium

COPY . .

RUN sudo useradd -m jobscoutuser
RUN sudo chown -R jobscoutuser:jobscoutuser /app
USER jobscoutuser

CMD ["sh", "-c", "celery -A app.celery_app worker --beat --loglevel=info"]