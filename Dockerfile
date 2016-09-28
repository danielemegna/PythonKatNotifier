FROM ubuntu:latest
#FROM resin/rpi-raspbian

RUN apt-get update && \
    apt-get install -y \
      python \
      python-pip

WORKDIR /tmp
COPY dependencies.prod .
RUN pip install -r dependencies.prod

WORKDIR /app
CMD ["python", "work.py"]
