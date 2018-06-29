FROM python:2-slim

RUN pip install --upgrade pip

WORKDIR /app
COPY . .
RUN cp empty.db production.db
RUN pip install -r requirements.txt

CMD ["python", "work.py"]
