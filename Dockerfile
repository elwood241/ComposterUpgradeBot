FROM python:3.12.1-bullseye

WORKDIR /opt
COPY main.py requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt --break-system-packages && \
    apt-get update && \
    apt-get install -y docker.io && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    chmod +x ./restart_bot.sh

CMD ["python", "./main.py"]