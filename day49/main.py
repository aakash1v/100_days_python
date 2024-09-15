from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

# URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
URL = 'https://www.linkedin.com/'

load_dotenv()

my_email = os.getenv('LINKEDIN_EMAIL')
my_password = os.getenv('LINKEDIN_PASSWORD')
my_number = os.getenv('MOBILE')

# keeping Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get(URL)
driver.find_element(By.CSS_SELECTOR, value='.nav .nav__button-secondary').click()

######### Logging in to linkedin... ########

email = driver.find_element(By.CSS_SELECTOR, value='#username')
email.send_keys(my_email)
password = driver.find_element(By.CSS_SELECTOR, value='#password')
password.send_keys(my_password, Keys.ENTER)

input("Press Enter when you have solved the Captcha")

search_bar = driver.find_element(By.CSS_SELECTOR, value='.search-global-typeahead__input')
search_bar.send_keys('python developer', Keys.ENTER)


# Locate the apply button
time.sleep(3)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=' .reusable-search__entity-cluster--quick-filter-action-container')
print(apply_button)

"""
driver.find_element(by=By.XPATH, value='')
# If application requires phone number and the field is empty, then fill in the number.

phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(my_number)

#Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
"""
