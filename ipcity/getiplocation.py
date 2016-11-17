import getip
import requests
import json
import logging

logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s: %(message)s', level=logging.DEBUG)

getiplocation_logger = logging.getLogger('getiplocation')


ip = getip.get_my_ip()


url = "http://geoip.nekudo.com/api/"+ip

response = requests.get(url)

def getiplocation(ip):
   if response.ok:
      getiplocation_logger.debug(response.content)
      data = json.loads(response.content)
      country = data['country']['code']
      city = data['city']
      getiplocation_logger.info("Location: " + city + ", "+country)
      return city, country

def getmyiplocation():
    return getiplocation(ip)

