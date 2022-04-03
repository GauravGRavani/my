import requests

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks://127.0.0.1:9050',
                       'https': 'socks://127.0.0.1:9050'}
    return session
#session = get_tor_session()

 #signal TOR for a new connection 
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="1")
        controller.signal(Signal.NEWNYM)
def showIP():
    print(session.get("http://httpbin.org/ip").text)
for i in range(5):
    renew_connection()
    session = get_tor_session()
    showIP()
    time.sleep(10)