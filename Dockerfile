FROM nginx
RUN apt update
RUN apt install git -y
RUN git clone https://github.com/clsacramento/myfirstgooglemap
RUN cp -R myfirstgooglemap/static/* /usr/share/nginx/html/.

