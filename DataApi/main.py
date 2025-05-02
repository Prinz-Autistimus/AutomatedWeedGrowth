from fastapi import FastAPI
import pigpio
import DHT22
import time

rpi = pigpio.pi()

light_tick_counter = 0

light_time = 5 #In Minutes
dark_time = 3 #InMinutes

DHT_PIN = 17
READ_RETRIES = 3
sensor = DHT22.sensor(rpi, DHT_PIN)

HEATER_PIN = 23
rpi.set_mode(HEATER_PIN, pigpio.OUTPUT)
heater_on = False

LAMP_PIN = 24
rpi.set_mode(LAMP_PIN, pigpio.OUTPUT)
lamp_on = False

app = FastAPI()

last_read = time.time() #Time in seconds
temp_cache = -100
hum_cache = -100

def read_sensor_values():
    global temp_cache, hum_cache, last_read
    if time.time() - last_read > 2:
        print("Calling Sensor for new Values")
        sensor._trigger()
        temp_cache = sensor._temperature
        hum_cache = sensor._humidity
        last_read = time.time()
    else:
        print("Read too fast, utilizing cached Values")

    print(f"Read sensor data: Temp:{temp_cache}°C, Humidity:{hum_cache}%")
    return (hum_cache, temp_cache)


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

#=================================================================================================#
#                                                                                                 #
#                                       REST-API ENDPOINTS                                        #
#                                                                                                 #
#=================================================================================================#

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/temp")
def read_temp():
    result: dict = {}
    
    _, temp = read_sensor_values()
    if not temp == -100:
        result.update({"temperature": temp})
    
    return result

@app.get("/humidity")
def read_humidity():
    result: dict = {}

    humidity, _ = read_sensor_values()
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

    humidity, temperature = read_sensor_values()

    result.update({"temperatur": temperature})
    result.update({"humidity": humidity})
    result.update({"lamp_on": 1 if lamp_on else 0})
    result.update({"heater_on": 1 if heater_on else 0})

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
def turn_off_lamp():
    global lamp_on
    lamp_before = lamp_on
    lamp_on = False
    apply_lamp()

    result: dict = {}

    result.update({"state_before": lamp_before})
    result.update({"state_after": lamp_on})
    return result    

@app.post("/tick")
def do_tick():
    global light_tick_counter
    before_tick = light_tick_counter
    light_tick_counter += 1

    if light_tick_counter > light_time+dark_time:
        light_tick_counter = 0


    if light_tick_counter <= light_time:
        if not lamp_on:
            turn_on_lamp()
    elif light_tick_counter > light_time and light_tick_counter <= light_time+dark_time:
        if lamp_on:
            turn_off_lamp()

    return {"last_tick": before_tick, "current_tick": light_tick_counter}
