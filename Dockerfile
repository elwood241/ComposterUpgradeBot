FROM python:3.12.1-bullseye

WORKDIR /opt
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]
