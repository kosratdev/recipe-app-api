FROM python:3.9-alpine
LABEL MAINTAINER="Kosrat Ahmed"

ENV PYTHONUNVUFFERED 1

COPY ./requirements /requirements
RUN pip install -r /requirements

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
