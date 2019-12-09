from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/selects2.html')
    id1 = browser.find_element_by_id('num1').text
    id2 = browser.find_element_by_id('num2').text
    val = int(id1) + int(id2)
    print(id1, id2)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(val))

    btn = browser.find_element_by_class_name('btn-default')
    btn.click()

    time.sleep(10)
