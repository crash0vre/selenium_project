from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get('http://automationpractice.com/index.php')
time.sleep(4)

#search_box=driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
search_box=driver.find_element(By.ID, 'search_query_top')
search_box.send_keys('dress')
time.sleep(2)
#search_box.send_keys(Keys.ENTER)
#click the Search button, finding by XPATH
#driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
search_box=driver.find_element(By.CSS_SELECTOR,'button.button-search').click()

"""search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('vita erendzhenov')
search_box.send_keys(Keys.ENTER)
time.sleep(5)"""

#driver.close()