from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pprint
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')

#my_store = []
#store = driver.find_elements(By.CSS_SELECTOR, value='#store div b')

"""
for ele in store:
    try:
        item, price = ele.text.split('-')
    except Exception as e:
        pass
    temp = {
        'item': item,
        'price': price
    }
    my_store.append(temp)
"""

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 2*60

while True:
    cookie.click()

    # Every 5 sec
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # creating dict to store items and prices..
        cookie_updates = {}
        for n in range(len(item_prices)):
            cookie_updates[item_prices[n]] = item_ids[n]

        # Get current cookie count..
        money = driver.find_element(By.ID, value='money').text
        if ',' in money:
            money = money.replace(',',"")
        cookie_count = int(money)

        # Find upgrades that we can currently afford..
        affordable_items = {}
        for cost, id in cookie_updates.items():
            if cookie_count > cost:
                affordable_items[cost] = id

        highest_price_affordable_items = max(affordable_items)
        print(highest_price_affordable_items)
        purchase_id = affordable_items[highest_price_affordable_items]

        driver.find_element(By.ID, value=purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5


    # After 2 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
