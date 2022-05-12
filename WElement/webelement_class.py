from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def initialize_driver():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(20)
    #driver.find_element(By.XPATH,"//input[@id='search_query_top']")
    return driver
#finding  the multiple elements
def webelement_properties(driver):
    driver.get('http://automationpractice.com')
    product_names = driver.find_elements(By.XPATH, "//span[normalize-space()='Add to cart']")
    #print(cart_buttons)
    time.sleep(3)
    print("Using the web element properties for each element")
    for cart_button in product_names:
        print('cart_button text: ',cart_button.text)
        print('cart_button size: ',cart_button.size)
        print('cart_button name: ',cart_button.tag_name)
    print('Number of elements ', len(product_names))
def close_browser(driver):
    time.sleep(5)
    driver.quit()
def webelement_metods(driver):
    #driver=webdriver.Chrome
    driver.get('http://automationpractice.com')
    #Enter 'Andrew'in search box then enter 'dress'
    search_box = driver.find_element(By.XPATH,"//input[@id='search_query_top']")
    search_box.send_keys('Andrew')
    time.sleep(3)
    search_box.clear()
    search_box.send_keys('dress')
    time.sleep(3)
    #Click search button
    compare_button = driver.find_element(By.XPATH,"//header/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]")
    time.sleep(1)
    #verify compare button is displate
    print("compare_button.is_displayed()", compare_button.is_displayed())

    #verify compare button is not enabled
    print("compare_button.is_enabled()", compare_button.is_enabled())

    #get attribute 'action' of compare
    print("Attribute of compare form", compare_button.get_attribute('action'))

def working_with_alerts(driver):
    driver.get('https://demoqa.com/alerts')
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
    alrt = driver.switch_to.alert
    time.sleep(2)
    alrt.accept()  # clicking Ok BUtton
    driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
    alrt = driver.switch_to.alert
    time.sleep(2)
    alrt.dismiss()
    driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
    alrt = driver.switch_to.alert
    alrt.send_keys("Hello world")
    time.sleep(3)
    alrt.accept()
    print('driver name: ', driver.name)
    print('Drive title: ', driver.title)
    driver.close()