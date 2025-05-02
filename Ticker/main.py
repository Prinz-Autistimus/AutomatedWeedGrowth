import requests
import time

while True:
    try:
        response = requests.post("http://192.168.178.68:8000/tick")
        print(f"Status: {response.status_code}, Antwort: {response.text}")
    except Exception as e:
        print(f"Fehler beim Senden: {e}")

    time.sleep(60 * 60)
