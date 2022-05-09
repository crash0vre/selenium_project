#Wdriver package, webdriver_class.py module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#initializing the chrome driver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10) #max wait time for all find elements
#properties for
driver.get('https://demoqa.com/browser-windows')

time.sleep(2)
print('Current url: ',driver.current_url)
print('driver.current_window_handle: ',driver.current_window_handle)
driver.back()
driver.refresh()
print('Current url: ',driver.current_url)
time.sleep(2)
driver.forward()
print('Current url: ',driver.current_url)
time.sleep(2)

driver.find_element(By.XPATH,"//button[@id='tabButton']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='windowButton']").click()
print('driver.window_handles: ',driver.window_handles)
print('Current URL: ',driver.current_url)
driver.switch_to.window(driver.window_handles[-1])

print('Current URL: ',driver.current_url)
time.sleep(3)
driver.close()
time.sleep(2)
driver.get('https://demoqa.com/alerts')
time.sleep(2)
driver.find_element(By.ID,'alertButton').click()
#driver.switch_to.window(driver.window_handles[-1])

#driver.quit()