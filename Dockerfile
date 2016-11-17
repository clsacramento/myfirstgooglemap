FROM python:3

MAINTAINER Cynthia Lopes do Sacramento "clsacramento@gmail.com"

RUN apt update
RUN apt install git -y
RUN git clone https://github.com/clsacramento/myfirstgooglemap
WORKDIR /myfirstgooglemap/ipcity
RUN ls
RUN pip install --no-cache-dir -r requirements.txt
CMD ['python', 'server.py']
