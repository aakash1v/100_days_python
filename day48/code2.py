from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrom browser open after program finishes..
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')


artice_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
#artice_count.click()

#Find element by link Text..
all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
#all_portals.click()
try:
    exit_button = driver.find_element(By.XPATH, value='//*[@id="vector-dark-mode-launch-banner"]/div/div[2]/header/button/span/svg')
    exit_button.click()
except Exception:
    pass

search_icon = driver.find_element(By.CSS_SELECTOR, name='search)
search_icon.click()

search = driver.find_element(By.CSS_SELECTOR, value='#searchform input')
search.send_keys('python')
search.send_keys(Keys.ENTER)
