# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /waste classify

COPY requirements.txt requirements.txt
RUN python3 --version  #untuk mengecek versi Python
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
