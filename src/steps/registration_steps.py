from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

def initialize_browser(browser):
    print(f'Init{browser} driver')
    driver=object
    if browser=="chrome":
        driver = webdriver.Chrome()
    if browser=="firefox":
        driver=webdriver.Firefox()
    driver.implicitly_wait(15)

    return driver

def open_website(driver,url):
    print("Opening website")
    driver.get(url)

def open_registration_form(driver,email):
    print("SignIn process <click sign in>")
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
    email_adress = driver.find_element(By.XPATH, "//input[@id='email_create']")
    email_adress.send_keys(email)
    driver.find_element(By.XPATH,
                        "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/button[1]/span[1]").click()
    time.sleep(5)
    assert 'account-creation' in driver.current_url, "account creation page failed"
    print('Account email', email)

def complete_registration_form(driver,phone_number,city,first_name,last_name,password,adress):
    # <<<gender_check>>>
    mr_title = driver.find_element(By.ID, 'id_gender1')
    mr_title.click()
    print("Creating castomer info")
    assert mr_title.is_selected(), "Mr was not selected"

    driver.find_element(By.ID, "customer_firstname").send_keys(first_name)
    time.sleep(2)
    # ad_firstname = driver.find_element(By.XPATH,"//input[@id='customer_firstname']").text
    # assert ad_firstname.strip() == first_name
    print('First name', first_name, "created")

    driver.find_element(By.XPATH, "//input[@id='customer_lastname']").send_keys(last_name)
    # ad_lastname = driver.find_element(By.XPATH,"//input[@id='customer_lastname']").text
    # assert ad_lastname.strip() == last_name
    print('Last name', last_name, 'created')
    driver.find_element(By.XPATH, "//input[@id='passwd']").send_keys(password)
    time.sleep(2)

    print("select Day '07' ")
    day_list = driver.find_element(By.ID, 'days')
    selection = Select(day_list)
    selection.select_by_index('7')

    print("select month 'October'")
    m_list = driver.find_element(By.XPATH, "//select[@id='months']")
    selection = Select(m_list)
    selection.select_by_index('10')

    print("Select year '1985'")
    y_list = driver.find_element(By.XPATH, "//select[@id='years']")
    selection = Select(y_list)
    selection.select_by_value('1985')

    print("Check Sign up for our newsletter! ")
    driver.find_element(By.ID, "newsletter").click()

    driver.find_element(By.XPATH, "//input[@id='address1']").send_keys(adress)
    print('Adress', adress, 'created')
    driver.find_element(By.XPATH, "//input[@id='city']").send_keys(city)
    print('City', city, 'created')
    time.sleep(3)
    print("Select state: first from the list")
    selection = Select(driver.find_element(By.ID, "id_state"))
    selection.select_by_index(1)
    driver.find_element(By.XPATH, "//input[@id='postcode']").send_keys(zip)
    print('Zip', zip, 'created')

    print('Select country: first from the list')
    selection = Select(driver.find_element(By.ID, "id_country"))
    selection.select_by_index(1)
    driver.find_element(By.XPATH, "//input[@id='phone_mobile']").send_keys(phone_number)
    print('Phone number', phone_number, 'created')
    primary = driver.find_element(By.ID, 'alias')
    primary.clear()
    primary.send_keys('Primary')

    driver.find_element(By.XPATH, "//span[normalize-space()='Register']").click()

def is_keyword_in_url(driver, keyword):
    assert keyword in driver.current_url, f"{keyword}  not verifiend"

def close_browser(driver):
    print("Closing website")
    time.sleep(2)
    driver.quit()