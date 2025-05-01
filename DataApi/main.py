from fastapi import FastAPI
import random
from pigpio_dht import DHT22
import pigpio
import time

rpi = pigpio.pi()

DHT_PIN = 17
READ_RETRIES = 1
sensor = DHT22(gpio=DHT_PIN, timeout_secs=2, use_internal_pullup=True, pi=rpi)

HEATER_PIN = 23
rpi.set_mode(HEATER_PIN, pigpio.OUTPUT)
heater_on = False

LAMP_PIN = 24
rpi.set_mode(LAMP_PIN, pigpio.OUTPUT)
lamp_on = False

app = FastAPI()

def read_sensor_values():
    result = sensor.read(READ_RETRIES)
    return result

def get_temp(sensor_data: dict):
    if not sensor_data["valid"]:
        return -100
        
    temp = sensor_data["temp_c"]
    return temp

def get_humidity(sensor_data: dict):
    if not sensor_data["valid"]:
        return -1
        
    humidity = sensor_data["humidity"]
    return humidity

def apply_heater():
    rpi.write(HEATER_PIN, 1 if heater_on else 0)

def apply_lamp():
    rpi.write(LAMP_PIN, 1 if lamp_on else 0)


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

@app.get("/lamp")
def read_lamp():
    result: dict = {"lamp_on": lamp_on}
    return result

@app.get("/heater")
def read_heater():
    result: dict = {"heater_on": heater_on}
    return result

@app.get("/status")
def read_status():
    result: dict = {}

    sensor_data = read_sensor_values()

    result.update({"temperatur": get_temp(sensor_data)})
    result.update({"humidity": get_humidity(sensor_data)})
    result.update({"lamp_on": lamp_on})
    result.update({"heater_on": heater_on})

    return result

@app.post("/heater/on")
def turn_on_heater():
    global heater_on
    heater_before = heater_on
    heater_on = True
    apply_heater()

    result: dict = {}

    result.update({"state_before": heater_before})
    result.update({"state_after": heater_on})
    return result

@app.post("/heater/off")
def turn_off_heater():
    global heater_on
    heater_before = heater_on
    heater_on = False
    apply_heater()

    result: dict = {}

    result.update({"state_before": heater_before})
    result.update({"state_after": heater_on})
    return result

@app.post("/lamp/on")
def turn_on_lamp():
    global lamp_on
    lamp_before = lamp_on
    lamp_on = True
    apply_lamp()
    
    result: dict = {}

    result.update({"state_before": lamp_before})
    result.update({"state_after": lamp_on})
    return result

@app.post("/lamp/off")
def turn_on_lamp():
    global lamp_on
    lamp_before = lamp_on
    lamp_on = False
    apply_lamp()

    result: dict = {}

    result.update({"state_before": lamp_before})
    result.update({"state_after": lamp_on})
    return result    