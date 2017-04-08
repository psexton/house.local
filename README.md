# house.local

Assorted bits of my quantified home

## Shared config

All components use a shared config file for reading in secret keys and other info. `exampleConfig.json` is an example of this file, with dummy values. Rename it to `net.psexton.house-local.json` and place it in `/etc/` to use.

## weather

Retrieves the temperature and apparent temperature (windchill in the winter, humidity-related heat in the summer) from [DarkSky](https://darksky.net/dev/), and uploads it to [Adafruit IO](https://io.adafruit.com/). Runs as a docker container.

You'll need: Docker, DarkSky API key, Adafruit IO API key.

More info at [Docker Hub](https://hub.docker.com/r/psexton/house-local-weather/).

## bedroom2

Reads in the temperature and humidity from a [AM2302](https://www.adafruit.com/products/393) sensor, and uploads it to [Adafruit IO](https://io.adafruit.com/). Because it needs to access the GPIO pins, it runs directly on the Pi, rather than in a Docker container.

You'll need: Raspberry Pi, AM2302 sensor, Python2, Adafruit IO API key.

Additional setup needed. See [adafruit/Adafruit_Python_DHT](https://github.com/adafruit/Adafruit_Python_DHT).
