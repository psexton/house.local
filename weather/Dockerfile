FROM alpine:latest
MAINTAINER paul@psexton.net

# Copy in script and set permissions
RUN mkdir /etc/periodic/1min
ADD announcer.sh /etc/periodic/1min/announcer
RUN chmod a+x /etc/periodic/1min/announcer

# Create a cron entry for 1min
RUN crontab -l | { echo "*       *       *       *       *       run-parts /etc/periodic/1min"; cat; } | crontab -

# Set cron in foreground as entrypoint
CMD crond -f
