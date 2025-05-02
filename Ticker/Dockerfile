FROM python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
  build-essential \
  python3-dev \
  python3-setuptools \
  curl \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Starte cron im Vordergrund
CMD ["python3", "./main.py"]