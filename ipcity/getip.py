import requests
import json
import logging
logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s: %(message)s', level=logging.DEBUG)

getip_logger = logging.getLogger('getip')

url = 'https://api.ipify.org?format=json'

def get_my_ip():
    response = requests.get(url)
    if response.ok:
        getip_logger.debug(response.content)
        data = json.loads(response.content)
        getip_logger.info("my ip is: "+ data['ip'])
    return data['ip']


