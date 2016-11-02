import getip
import requests
import json

ip = getip.get_my_ip()


url = "http://geoip.nekudo.com/api/"+ip

response = requests.get(url)

if response.ok:
   print response.content
   data = json.loads(response.content)
   print data['country']['code']
   print data['city']
