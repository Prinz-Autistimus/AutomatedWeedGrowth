# Automated Weed Growth

This All-In-One Solution will help you monitor your seed for a good harvest. 

## Motivation

I recently started learning about growing your own weed and because i'm studying Software Engineering i thought: "Why not automate that?".

Because i still have no idea what you have to look out for when growing your own weed, this software will be less of a finished product but more like a journey.

## Requirements
- Raspberry Pi
- Sensors (Humidity, Temperature)
- Electronic Valves (Solenoid Valves)
- Grow Lamp
  
(This list will be updated once i am more familiar with the equipment needed )

## Idea
A Raspberry Pi with suitable sensors will be used to monitor different metrics like humidity and temperatur to ensure that your seedling is growing optimal.

In addition, you should be able to hook up a grow lamp and a water valve to automate the day-night light intervals and watering.

## Implementation
A Docker-Container with a simple FastApi program will sit sit right beside your plant. You can either ask different metrics from this API or ask it to do things like "start watering" or "turn off grow lamp". This ensure direct interaction with your plant.
All external equipment will be hooked up either directly or via a breakout board like a Relais-Board.

Another Docker-Container should host a webapp which will communicate with this API. It will constantly pull data from the endpoint and store it in a database to create a visual representation of the metrics. You will also be able to perform certain actions through simple button presses like "Water my plant with 2L of water".

## Community
This is an open-source product which will be available for everybody to use to their own liking. Feel free to help this project by opening issues or contact me if you think something isn't right.