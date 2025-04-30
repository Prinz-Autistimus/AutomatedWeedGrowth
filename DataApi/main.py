from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/temp")
def read_temp():
    result: dict = {}

    for i in range(50):
        try:
            temp = sensor.temperature
            result.update({"temperature": f"{temp}"})
            break
        except:
            print("Error while reading temperature, Attempt: " + i)
    
    return result

@app.get("/humidity")
def read_humidity():
    result: dict = {}

    for i in range(50):
        try:
            humidity = sensor.humidity
            result.update({"humidity": f"{humidity}"})
            break
        except:
            print("Error while reading humidity, Attempt: " + i)

    return result

@app.get("/status")
def read_status():
    result: dict = {}

    result.update({"temperatur": 20})
    result.update({"humidity": 50})
    result.update({"lamp_on": True})
    result.update({"heater_on": False})

    return result
