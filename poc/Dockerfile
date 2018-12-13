FROM python:3.6-slim

# C compiler (gcc) is needed to install uwsgi. 
# 'ps' and 'curl' are helpful for troubleshooting.
RUN apt update && apt install -y procps curl gcc

# Python libs
RUN pip install --no-cache-dir uwsgi flask requests

# Our app
COPY ./src /opt/cms-monit

