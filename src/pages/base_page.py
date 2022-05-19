from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:


    def __init__(self,driver):
        #driver = webdriver.Chrome()
        self.driver = driver
        self.wdwait = WebDriverWait(driver,10)

    def click_element_by_id(self,id):
        try:
            element = self.driver.find_element(By.ID,id)
            element = self.wdwait.until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            print(f'Error in click element by ID, please check, {id}')
            print(f'Error message,{err}')

    def click_element_by_XP(self, xp):
        try:
            self.wdwait.until(EC.element_to_be_clickable((By.XPATH, xp))).click()
        except (NoSuchElementException, TimeoutException) as err:
            print(f'Error in click element by ID, please check, {xp}')
            print(f'Error message,{err}')


    def enter_text_by_id(self,id, text):
        try:
            element = self.wdwait.until(EC.element_to_be_clickable((By.ID, id))).clear()
            element.click(text)
        except (NoSuchElementException, TimeoutException) as err:
            print(f'Error in click element by text, please check, {id}')

    def select_from_dropdown_by_id_and_value(self,id,index_value):
        try:
            element = self.wdwait.until(EC.element_to_be_clickable((By.ID, id)))
            selection = Select(element) # finde element with Select tagname
            selection.select_by_index(1) #index: '-'s 0, next option will me index1
        except (NoSuchElementException, TimeoutException) as err:
            print(f'Error in selecting dropdown ID, please check, {id}')



