import requests
import time

UPPER_LIMIT = 24
LOWER_LIMIT = 22

while True:
    try:
        temp_response = requests.get("http://192.168.178.68:8000/temp")
        heater_response = requests.get("http://192.168.178.68:8000/heater")

        print(f"Status Temp: {temp_response.status_code}, Antwort: {temp_response.text}")
        print(f"Status Heater: {heater_response.status_code}, Antwort: {heater_response.text}")
        
        if temp_response.ok and heater_response.ok:
            temp_json = temp_response.json()
            temp = temp_json.get("temperature")

            heater_json = heater_response.json()
            heater_on = heater_json.get("heater_on")

            endpoint = ""

            if temp < LOWER_LIMIT and not heater_on:
                endpoint = "http://192.168.178.68:8000/heater/on"
            elif temp > UPPER_LIMIT and heater_on:
                endpoint = "http://192.168.178.68:8000/heater/off"
            else:
                continue

            answer = requests.post(endpoint)

            print(f"Status after action: {answer.text}")
    except Exception as e:
        print(f"Fehler beim Senden: {e}")

    time.sleep(5)