# house.local

Assorted bits of my quantified home

## Shared config

All components use a shared config file for reading in secret keys and other info. `exampleConfig.json` is an example of this file, with dummy values. Rename it to `net.psexton.house-local.json` and place it in `/etc/` to use.

## weather

Retrieves the temperature and apparent temperature (windchill in the winter, humidity-related heat in the summer) from [DarkSky](https://darksky.net/dev/), and uploads it to [Adafruit IO](https://io.adafruit.com/). Runs as a docker container.
