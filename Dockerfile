FROM python:3.7-alpine
LABEL Gaurav Shankar

#This allows python to run in unbuffered mode which
#is recommended when you are running python in docker mode
#It doesnt allow python to buffer output and print directly
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./app /app

#adduser will create a user and -D 
#says that create a user which is used of running only
#not for home directory

#we do this for security purposes, so that it not run as root user
RUN adduser -D user
USER user


