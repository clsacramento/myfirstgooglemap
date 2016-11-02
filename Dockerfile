FROM nginx

MAINTAINER Cynthia Lopes do Sacramento "clsacramento@gmail.com"

RUN apt update
RUN apt install git -y
RUN git clone https://github.com/clsacramento/myfirstgooglemap
RUN cp -R myfirstgooglemap/static/* /usr/share/nginx/html/.
CMD ["sh", "-c", "cd myfirstgooglemap; git pull; nginx -g 'daemon off;'"]
