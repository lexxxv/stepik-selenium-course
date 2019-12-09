from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://SunInJuly.github.io/execute_script.html')

    id_x = browser.find_element_by_id('input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", id_x)
    res = calc(id_x.text)

    input_fld = browser.find_element_by_id('answer')
    input_fld.send_keys(res)

    cb_elt = browser.find_element_by_id('robotCheckbox')
    cb_elt.click()

    rb_elt = browser.find_element_by_id('robotsRule')
    rb_elt.click()

    btn = browser.find_element_by_css_selector('.btn.btn-primary')
    btn.click()

    time.sleep(10)
