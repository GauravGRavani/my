import requests
from stem import Signal
from stem.control import Controller
import time


def get_tor_session():
    # Tor uses the 9050 port as the default socks port
    proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
   }
    

    headers = {}
 
   v = requests.get('http://httpbin.org/ip', proxies=proxies,headers=headers)
   print(v.text)
#session = get_tor_session()

 #signal TOR for a new connection 
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="1")
        controller.signal(Signal.NEWNYM)
for i in range(5):
    renew_connection()
    get_tor_session()
    time.sleep(10)