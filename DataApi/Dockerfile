FROM python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
  gcc \
  g++ \
  git \
  build-essential \
  python3-dev \
  python3-setuptools \
  libffi-dev \
  libssl-dev \
  make \
  wget \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git && \
    cd Adafruit_Python_DHT && \
    python3 setup.py install --force-pi && \
    cd .. && rm -rf Adafruit_Python_DHT

COPY . /app

EXPOSE 8000

CMD ["fastapi", "run", "/app/main.py", "--port", "8000"]
