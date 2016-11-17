from flask import Flask
from flask import render_template
import os
import getiplocation
app = Flask(__name__)

try:
    port = os.environ['PORT']
except KeyError:
    port = 5000

@app.route("/")
def printmap():
    (city,country) = getiplocation.getmyiplocation()
    return render_template('index.html',_city=city,_country=country)
    return "Hello World! City: "+city+", Country: "+country

if __name__ == "__main__":
    app.run(port=port)
