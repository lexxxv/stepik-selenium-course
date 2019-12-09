from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    inp_elt = browser.find_element_by_id('answer')
    inp_elt.send_keys(y)

    cb_elt = browser.find_element_by_id('robotCheckbox')
    cb_elt.click()

    rb_elt = browser.find_element_by_id('robotsRule')
    rb_elt.click()

    btn = browser.find_element_by_class_name('btn-default')
    btn.click()

    time.sleep(10)