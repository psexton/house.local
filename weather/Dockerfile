FROM python:3.6-alpine
MAINTAINER paul@psexton.net

# Install Python modules
RUN pip3 install requests adafruit-io

# Create a cron entry for 1min
RUN mkdir /etc/periodic/1min
RUN crontab -l | { echo "*       *       *       *       *       run-parts /etc/periodic/1min"; cat; } | crontab -

# Copy in script and set permissions
ADD announcer.py /etc/periodic/1min/announcer
RUN chmod a+x /etc/periodic/1min/announcer

# Set cron in foreground as entrypoint
CMD crond -f
