from selenium import webdriver  
import time
 driver = webdriver.Firefox(executable_path=r'home/kali/Downloads)
driver.get('https://www.lifeofpentester.blogspot.com')
time.sleep(4)
# insert time.sleep() here  
driver.close()