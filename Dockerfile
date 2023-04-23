FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
   && apk add postgresql-dev gcc musl-dev jpeg-dev zlib-dev

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install --no-cache-dir -r requirements.txt


COPY . .