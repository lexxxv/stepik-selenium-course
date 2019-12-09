from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)

    browser.get('http://suninjuly.github.io/redirect_accept.html')

    # time.sleep(3)

    btn = browser.find_element_by_css_selector('.trollface.btn.btn-primary')
    btn.click()

    # time.sleep(3)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    id_x = browser.find_element_by_id('input_value')
    res = calc(id_x.text)

    input_fld = browser.find_element_by_id('answer')
    input_fld.send_keys(res)

    btn2 = browser.find_element_by_css_selector('.btn.btn-primary')
    btn2.click()

    time.sleep(10)
