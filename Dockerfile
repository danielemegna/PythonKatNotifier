FROM ubuntu:latest
#FROM resin/rpi-raspbian

RUN apt-get update && \
    apt-get install -y \
      python \
      python-pip
RUN pip install --upgrade pip

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
CMD ["python", "work.py"]
