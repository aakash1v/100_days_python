from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()

driver.get('https://secure-retreat-92358.herokuapp.com/')


fname = driver.find_element(By.NAME, value='fName')
fname.send_keys('Aakash')
lname = driver.find_element(By.NAME, value='lName')
lname.send_keys('Kumar')
email = driver.find_element(By.NAME, value='email')
email.send_keys('aakashkumar@gmail.com')

btn = driver.find_element(By.CLASS_NAME, value='btn')
btn.click()


