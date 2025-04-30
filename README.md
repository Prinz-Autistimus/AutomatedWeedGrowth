# Automated Weed Growth

This All-In-One Solution will help you monitor your seed for a good harvest. 

## Motivation

I recently started learning about growing your own weed and because i'm studying Software Engineering i thought: "Why not automate that?".

Because i still have no idea what you have to look out for when growing your own weed, this software will be less of a finished product but more like a journey.

## Requirements
- Raspberry Pi
- Sensors (Humidity, Temperature)
- 12V Electric Pump (DC)
- Grow Lamp
- Electric Heater
  
(This list will be updated once i am more familiar with the equipment needed )

## Idea
A Raspberry Pi with suitable sensors will be used to monitor different metrics like humidity and temperatur to ensure that your seedling is growing optimal.

In addition, you should be able to hook up a grow lamp and a water pump to automate the day-night light intervals and watering.

A Docker-Container with a simple FastApi program will sit right beside your plant. You can either ask different metrics from this API or ask it to do things like "start watering" or "turn off grow lamp". This ensure direct interaction with your plant.
All external equipment will be hooked up either directly or via a breakout board like a Relais-Board.

Another Container Stack should host a webapp which will communicate with this API. It will constantly pull data from the endpoint and store it in a database to create a visual representation of the metrics. You will also be able to perform certain actions through simple button presses like "Water my plant with 2L of water".

## Implementation
A Container Stack with Grafana and InfluxDB will be used to visualize your metrics. The InfluxDB stores data like temperature, humidity, lamp_on/off, heater_on/off, water_on/off.

This information is provided by the data_api which is run in a docker container with an image compiled for arm64 (for the raspberry pi with RaspiOS Lite 64-Bit).

A telegraf instance, which is developed by the team from the influxDB, is used, to periodically pull data from the Data API, which will provide the metrics in a JSON format. This data is automatically parsed and pushed into the Database.

Grafana OSS is used to visualize your data. It is connected to the InfluxDB via an API token and pulls data from your database and converts it to visually appealing graphs.


## Community
This is an open-source product which will be available for everybody to use to their own liking. Feel free to help this project by opening issues or contact me if you think something isn't right.