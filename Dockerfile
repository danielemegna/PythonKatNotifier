FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
      python \
      python-pip
RUN pip install --upgrade pip

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "work.py"]
