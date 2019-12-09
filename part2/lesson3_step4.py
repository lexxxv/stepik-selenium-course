from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/alert_accept.html')

    btn = browser.find_element_by_css_selector('.btn.btn-primary')
    btn.click()

    alert = browser.switch_to.alert
    alert.accept()

    id_x = browser.find_element_by_id('input_value')
    res = calc(id_x.text)

    input_fld = browser.find_element_by_id('answer')
    input_fld.send_keys(res)

    btn2 = browser.find_element_by_css_selector('.btn.btn-primary')
    btn2.click()

    time.sleep(10)
