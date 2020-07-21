from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(10)

cookie = driver.find_element_by_id('bigCookie')
cookies_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id('productPrice' + str(item)) for item in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookies_count.text.split(' ')[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value < count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()

