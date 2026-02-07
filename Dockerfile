FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    VIRTUAL_ENV=/opt/venv \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt .

RUN python -m venv $VIRTUAL_ENV \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Install Playwright only if the environment variable PLAYWRIGHT_INSTALL is set
RUN if [ "$PLAYWRIGHT_INSTALL" = "true" ]; then \
        python -m playwright install chromium --with-deps --only-shell; \
    fi

COPY . .

RUN useradd -m appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /app /data

RUN if [ "$PLAYWRIGHT_INSTALL" = "true" ]; then \
        chown -R appuser:appuser /ms-playwright; \
    fi

USER appuser