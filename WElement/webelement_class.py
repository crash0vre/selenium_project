from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    time.sleep(7)
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

def test_explicit_way(driver):
    driver= webdriver.Chrome()
    wdwait = WebDriverWait(driver, 20)  # step 1
    print('<<<Text explisit wait>>>')
    print("oprning website")
    driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
    print('get initial text')
    #original_msg=driver.find_element(By.ID,'h2').text #option 1
    original_msg= wdwait.until(EC.presence_of_element_located((By.ID,"h2"))).text #option 2
    print(f'Original message displayed: {original_msg}')

    print('Click on "Change text to ... " button')
    driver.find_element(By.ID,"populate-text").click()

    print("Wait ubtil text is present 'Selenium Webdriver' maxx wait time is 20")

    wdwait.until(EC.text_to_be_present_in_element((By.ID,'h2'),'Selenium')) #step 2
    target_msg = driver.find_element(By.ID, 'h2').text
    print(f"Target text: {target_msg}")

    print("<<<Wait untill second button to be enabled for clicking>>>")
    print(f"Checking the button: {driver.find_element(By.ID, 'disable').is_enabled()}")
    if not driver.find_element(By.ID, 'disable').is_enabled():
        driver.find_element(By.ID, "enable-button").click()
    wdwait.until(EC.element_to_be_clickable((By.ID,"disable")))
    driver.find_element(By.ID, 'disable').click()
    print("Element is clickable after 10 sec")


def test_drag_and_drop(driver):
    #driver=webdriver.Chrome()
    driver.implicitly_wait(20)
    wdwait=WebDriverWait(driver,10)

#1. Open site
    print('Open website')
    url='https://jqueryui.com/droppable/'
    driver.get(url)
    wdwait.until(EC.presence_of_element_located((By.ID, "content")))
#2.Find draggable element
    driver.switch_to.frame(0)
    element1=driver.find_element(By.ID,"draggable")
    print('Element found',{element1.text})
#3.Find droppble box where we need to drop first element
    #element2=driver.find_element(By.ID,'droppable') #optinon 1
    element2=wdwait.until(EC.presence_of_element_located((By.ID,"droppable"))) #option 2
    print('Second element found',{element2.text})

#4.Perfom drag and drop action
    action=ActionChains(driver)
    action.drag_and_drop(element1,element2).perform()
    assert 'Dropped' in element2.text, "Drag and drop action are failed"
#5.Check the text after the action
    print(f"Text in target element: {element2.text}")

def test_hover_over_action(driver):
    pass
