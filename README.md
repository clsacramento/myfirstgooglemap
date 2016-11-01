# myfirstgooglemap

Just an html example using javascript to plot a google maps pointing to specified city.

## How to use
Simply open static/index.html with a browser.

Alternatively, you can place the content on a web server like nginx or any other.

## Docker
To test it on a nginx web server using docker, you can use the following command:

~~~
docker run clsacramento/myfirstgooglemap -p 8080:80 -d
~~~

You can also build your own docker image with the Dockerfile provided:

~~~
git clone https://github.com/clsacramento/myfirstgooglemap
cd myfirstgooglemap
docker build -t myfirstgooglemap . 
~~~
