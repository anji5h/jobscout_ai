FROM python:3.12-slim

WORKDIR /app

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium

COPY . .

RUN useradd -m jobscoutuser
RUN mkdir -p /data
RUN chown -R jobscoutuser:jobscoutuser /app /data /ms-playwright
USER jobscoutuser

CMD ["celery", "-A", "app.celery_app", "worker", "--beat", "--loglevel=info"]