from fastapi import FastAPI
import random
from pigpio_dht import DHT22
import pigpio
import time

DHT_PIN = 17
READ_RETRIES = 5
sensor = DHT22(DHT_PIN)

app = FastAPI()
pi = pigpio.pi()

def read_sensor_values():
    result = sensor.read(READ_RETRIES)
    return result

def get_temp():
    sensor_data = read_sensor_values()

    if not sensor_data["valid"]:
        return -100
        
    temp = sensor_data["temp_c"]
    return temp

def get_humidity():
    sensor_data = read_sensor_values()

    if not sensor_data["valid"]:
        return -1
        
    humidity = sensor_data["humidity"]
    return humidity


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/temp")
def read_temp():
    result: dict = {}
    
    temp = get_temp()
    if not temp == -100:
        result.update({"temperature": temp})
    
    return result

@app.get("/humidity")
def read_humidity():
    result: dict = {}

    humidity = get_humidity()
    if not humidity == -1:
        result.update({"humidity": humidity})
    
    return result

@app.get("/status")
def read_status():
    result: dict = {}

    result.update({"temperatur": get_temp()})
    result.update({"humidity": get_humidity()})
    result.update({"lamp_on": False})
    result.update({"heater_on": False})

    return result