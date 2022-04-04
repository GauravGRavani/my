from selenium import webdriver  
from selenium.webdriver.firefox.firefox\_binary import FirefoxBinary  
binary = FirefoxBinary('/root/Downloads/firefox/firefox')  
driver = webdriver.Firefox(firefox\_binary=binary)  
driver.get('https://www.lifeofpentester.blogspot.com')
# insert time.sleep() here  
driver.close()