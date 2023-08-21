FROM ubuntu:latest

WORKDIR /webwav

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt /webwav/requirements.txt
RUN python3 -m pip install -r /webwav/requirements.txt
COPY . /webwav/

EXPOSE 8886

#CMD python3 /webwav/myapp.py