import requests
get = requests.get('https://httpbin.org/ip')
get.text
print(get.text)