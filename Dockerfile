FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    VIRTUAL_ENV=/opt/venv \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    supervisor \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m venv $VIRTUAL_ENV \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python -m playwright install chromium --with-deps --only-shell

COPY . .
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN useradd -m appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /app /data /ms-playwright /etc/supervisor

USER appuser

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]