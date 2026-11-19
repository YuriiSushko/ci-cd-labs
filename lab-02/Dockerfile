FROM python:3.12-slim

RUN useradd --create-home --uid 6767 app 
RUN mkdir -p /data && chown app:app /data

USER app

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV PORT=8080
ENV COUNTER_FILE=./data/visits.txt

EXPOSE 8080

CMD ["python", "app.py"]