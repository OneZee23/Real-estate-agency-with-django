# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /agency
COPY requirements.txt /agency/
RUN pip install -r requirements.txt
COPY . /agency/
