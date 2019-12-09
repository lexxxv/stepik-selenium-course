from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    # browser.implicitly_wait(5)

    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    btn = browser.find_element_by_id("book")
    btn.click()

    id_x = browser.find_element_by_id('input_value')
    res = calc(id_x.text)

    input_fld = browser.find_element_by_id('answer')
    input_fld.send_keys(res)

    btn2 = browser.find_element_by_id('solve')
    btn2.click()



    time.sleep(10)
