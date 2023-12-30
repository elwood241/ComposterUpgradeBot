FROM python:3.12.1-bullseye

WORKDIR /opt
COPY . .
RUN pip install -r requirements.txt --break-system-packages
CMD ["python", "./main.py"]
