FROM python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
  gcc \
  g++ \
  python3-dev \
  python3-setuptools \
  libffi-dev \
  libssl-dev \
  make \
  wget \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.7.1.tar.gz && \
  tar -xzf RPi.GPIO-0.7.1.tar.gz && \
  cd RPi.GPIO-0.7.1 && \
  python3 setup.py install && \
  cd .. && rm -rf RPi.GPIO*

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD ["fastapi", "run", "/app/main.py", "--port", "8000"]
