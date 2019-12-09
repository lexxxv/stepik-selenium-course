from selenium import webdriver
import time
import os

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/file_input.html')

    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Lexx')

    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('V')

    email = browser.find_element_by_name('email')
    email.send_keys('lexx@v')

    file_btn = browser.find_element_by_id('file')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'try.txt')           # добавляем к этому пути имя файла
    file_btn.send_keys(file_path)

    btn = browser.find_element_by_css_selector('.btn.btn-primary')
    btn.click()

    time.sleep(10)
