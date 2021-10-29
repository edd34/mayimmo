# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY components /code/
COPY mayimmo /code/
COPY utils /code/
COPY manage.py /code/
