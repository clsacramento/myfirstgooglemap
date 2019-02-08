from flask import Flask
from flask import render_template
import os
import random
import getiplocation
import load_zones

app = Flask(__name__)

try:
    port = os.environ['PORT']
except KeyError:
    port = 5000


try:
    key = '&key='+os.environ['KEY']
except KeyError:
    key = ''

@app.route("/")
def printmap():
    zones = load_zones.get_zones_locations()
    index = random.randint(0,len(zones)-1)
    (city,country) = zones[index]
    return render_template('index.html',_city=city,_country=country,_key=key)
    return "Hello World! City: "+city+", Country: "+country

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port)
