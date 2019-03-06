FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src
ADD requirements.txt /src

RUN pip install --upgrade pip \
&& apk update \
&& apk add build-base \
&& pip install --no-cache-dir -r /src/requirements.txt \
&& apk del build-base \
&& rm -rf /var/cache/apk/*

COPY ./demo /src/
WORKDIR /src

