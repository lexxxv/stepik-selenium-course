# import math
# fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
# print(fun(5))

import time
from selenium import webdriver


driver = webdriver.Chrome()

time.sleep(5)

driver.get('https://wiki.corp.motiv/')
time.sleep(5)

textarea = driver.find_element_by_css_selector(".text.app-search.search.quick-search-query")

textarea.send_keys("Jenkins")
time.sleep(5)

submit_button = driver.find_elements_by_css_selector("[id='quick-search-submit']")

submit_button.click()
time.sleep(5)

driver.quit()