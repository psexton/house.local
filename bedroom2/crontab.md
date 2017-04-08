# Cron Usage

Your crontab file should look something like this:

```
# m h  dom mon dow   command
*/15 * * * * /home/pi/house.local/bedroom2/read_sensor_and_upload.py
```
