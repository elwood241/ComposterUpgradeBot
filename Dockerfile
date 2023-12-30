FROM python:3.12.1-bullseye

WORKDIR /opt
COPY . .


RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir requests && \
    pip install --no-cache-dir mysql.connector && \
    apt-get update && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["python", "./main.py"]