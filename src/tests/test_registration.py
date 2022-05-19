from src.pages.base_page import *
from src.steps.registration_steps import *
from src.utilities import *

#Var
data=load_yaml_file(f"../../data/config.yml")
first_name=data['first_name']
last_name=data['last_name']
password=data['password']
adress=data['adress']
city=data['city']
phone_number=data['phone_number']
email=f"user{get_timestamp()}@ail.com"
url=data['url']

#Scenario
print("Test case steps")
driver = initialize_browser('chrome')
open_website(driver,url)
open_registration_form(driver,email)
complete_registration_form(driver,first_name,last_name,password,adress,city,phone_number)
#is_keyword_in_url(driver,)
close_browser(driver)


