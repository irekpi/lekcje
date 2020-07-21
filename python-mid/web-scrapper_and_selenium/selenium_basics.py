from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.python.org")

#passing the searching Phrase
search = driver.find_element_by_name('q')
search.clear()
search.send_keys('pycon')
search.send_keys(Keys.RETURN)

try:
    section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'main-content '))
    )
    articles = section.find_elements_by_tag_name('li')
    for item in articles:
        print(item.text)
finally:
    driver.quit()


