from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    # browser.implicitly_wait(5)

    browser.get('http://suninjuly.github.io/cats.html')

    btn = browser.find_element_by_id("button")

    time.sleep(10)
