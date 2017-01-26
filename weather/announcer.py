#!/usr/bin/env python3

import datetime
import json
import requests
import Adafruit_IO

print("Ran at", datetime.datetime.now())

# Read in the json config
# Found at /etc/net.psexton.house-local-weather.json
with open('/etc/net.psexton.house-local-weather.json') as config_file:
    config_data = json.load(config_file)

# Read in the weather forecast
url = ("https://api.darksky.net/forecast"
       + "/" + config_data["darkSkySecretKey"]
       + "/" + config_data["latitude"]
       + "," + config_data["longitude"]
       + "?exclude=minutely,hourly,daily,alerts,flags")
response = requests.get(url).json()

# We want to pull out two values from the response json:
# currently.temperature and currently.apparentTemperature
temperature_f = response["currently"]["temperature"]
apparent_temperature_f = response["currently"]["apparentTemperature"]

# Send them up to adafruit.io
aio = Adafruit_IO.Client(config_data["adafruitIoKey"])
aio.send("weather-temperature-f", temperature_f)
aio.send("weather-apparent-temperature-f", apparent_temperature_f)
