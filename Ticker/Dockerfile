FROM debian:bookworm-slim

# Installiere cron und curl
RUN apt-get update && apt-get install -y cron curl

# Cronjob hinzufügen (jede Minute ein POST-Request)
RUN echo "* * * * * curl -X POST http://192.168.178.68:8000/tick >> /etc/crontab

# Starte cron im Vordergrund
CMD ["cron", "-f"]