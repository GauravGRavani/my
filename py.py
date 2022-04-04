import requests
from stem import Signal
from stem.control import Controller
import time
import random

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
refer_url_list =['https://gauravravani3.blogspot.com/hy/',
'https://saunak.com/g/',
'https://gaurav.saunak.com/gau/',
'https://diya.gt/',
'https://httpbin.gk/hak/jel/']

url = ['https://floralrichardapprentice.com/avbm4di2p?key=b0f8552768c6f1bab80f53dc8b8c6a11',
   'https://floralrichardapprentice.com/hdqidfgyu4?key=a9a833792291df485ce1ddfaa1e0a84f','https://floralrichardapprentice.com/y7ty2ahn9?key=1023b57681b849c59097df91aefe5860','https://floralrichardapprentice.com/dcvteb4s?key=e30a30da43b1d4c9fe8129f35db6c27c','https://floralrichardapprentice.com/pb5mqp2ke?key=46c2d7f8be42e598e52e659230393d80','https://floralrichardapprentice.com/fszjfysr4?key=cfb1a02416ba0a3a3a913ab347777b3d','https://floralrichardapprentice.com/qi0z2fb2jf?key=9ea96e33225a3592a2707a6c8decaba7']

def get_tor_session():
    bcurl = random.randrange(3907688, 976577876668)+'.html'
    user_agent = random.choice(user_agent_list)
    referurl = random.choice(refer_url_list) + bcurl
    url1 = random.choice(url)
    # Tor uses the 9050 port as the default socks port
    proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
   }
    

    headers = {'User-Agent': user_agent,
                'Referer': referurl
    }
 
   v = requests.get('http://httpbin.org/headers', proxies=proxies,headers=headers,allow_redirects=True)
   print(v.text)
#session = get_tor_session()

 #signal TOR for a new connection 
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="1")
        controller.signal(Signal.NEWNYM)
while True:
    renew_connection()
    get_tor_session()
    time.sleep(5)