# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN python -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim AS runtime

RUN useradd --create-home --uid 6767 app
RUN mkdir -p /data && chown app:app /data

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENV PORT=8080
ENV COUNTER_FILE=/data/visits.txt

WORKDIR /app

COPY --chown=app:app app.py .

USER app

EXPOSE 8080

CMD ["python", "app.py"]
