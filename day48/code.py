from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint


driver = webdriver.Chrome()
driver.get('https://python.org')


date_list = [date.text for date in  driver.find_elements(By.CSS_SELECTOR, value='.event-widget .menu time')]
title_list  = [title.text for title in  driver.find_elements(By.CSS_SELECTOR, value='.event-widget .menu a')]

events = {}

for i in range(len(date_list)):
    events[i] = {'time': date_list[i], 'events': title_list[i]}

pprint.pp(events)

