FROM arm32v7/python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y gcc python3-dev

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD ["fastapi", "run", "/app/main.py", "--port", "8000"]
