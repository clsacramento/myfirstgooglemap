FROM python:2

MAINTAINER Cynthia Lopes do Sacramento "clsacramento@gmail.com"

RUN apt update
RUN apt install vim -y #useful for debugging
COPY . /myfirstgooglemap
WORKDIR /myfirstgooglemap/cities
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./server.py" ]
