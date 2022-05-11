from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#driver.maximize_window()
driver.implicitly_wait(20)
#finding  the multiple elements
driver.get('http://automationpractice.com')
product_names = driver.find_elements(By.XPATH, "//span[normalize-space()='Add to cart']")
#print(cart_buttons)
time.sleep(3)
for cart_button in product_names:
    print('cart_button text: ',cart_button.text)
    print('cart_button size: ',cart_button.size)
    print('cart_button name: ',cart_button.tag_name)
print('Number of elements ', len(product_names))

time.sleep(3)
driver.quit()
