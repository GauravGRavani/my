from selenium import webdriver  
 driver = webdriver.Firefox(executable_path=r'home/kali/Downloads)
driver.get('https://www.lifeofpentester.blogspot.com')
# insert time.sleep() here  
driver.close()