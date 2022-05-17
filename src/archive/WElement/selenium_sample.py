from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get('https://www.visualophthalmologyservices.com/')
time.sleep(4)

search_box = driver.find_element(By.NAME,'q')
#search_box.send_keys('vita erendzhenov')
search_box.send_keys(Keys.ENTER)
time.sleep(5)

driver.close()
