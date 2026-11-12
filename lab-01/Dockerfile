FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

ENV PORT=8080
ENV COUNTER_FILE=./data/visits.txt

EXPOSE 8080

CMD ["python", "app.py"]