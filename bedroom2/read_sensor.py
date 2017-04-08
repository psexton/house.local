#!/usr/bin/python
# Author: Paul Sexton
# Based on AdafruitDHT.py, licensed as follows:
#
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import json
import Adafruit_DHT

# No need to parse command line parameters - we're not going to be swapping sensors or GPIO pins
sensor = Adafruit_DHT.AM2302
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperatureC = Adafruit_DHT.read_retry(sensor, pin)

# Adafruit DHT library returns temperature in Celsius. Also provide Fahrenheit in our output
temperatureF = temperatureC * 9/5.0 + 32

# Round all values to 1 decimal place
temperatureC = round(temperatureC, 1)
temperatureF = round(temperatureF, 1)
humidity = round(humidity, 1)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperatureC is not None:
    # Output success json
    print json.dumps({'success': True, 'celsius': temperatureC, 'fahrenheit': temperatureF, 'humidity': humidity})
else:
    # Output failure json, set process exit code to 1
    print json.dumps({'success': False})
    sys.exit(1)
