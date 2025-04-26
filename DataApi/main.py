from fastapi import FastAPI
import random
import adafruit_dht
import board

sensor = adafruit_dht.DHT22(board.D4)
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
