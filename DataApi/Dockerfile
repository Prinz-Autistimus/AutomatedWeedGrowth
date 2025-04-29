FROM arm32v7/python:3.13-slim-bullseye

WORKDIR /app

RUN apk add --no-cache gcc musl-dev python3-dev

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD ["fastapi", "run", "/app/main.py", "--port", "8000"]