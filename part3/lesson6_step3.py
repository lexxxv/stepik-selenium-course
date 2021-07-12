import time
import math
from selenium import webdriver
import pytest

list_url = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]

@pytest.fixture
def browser():
    print("\nstart browser..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("browser close")
    browser.quit()

@pytest.mark.parametrize('link', list_url)
def test_findletter(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_tag_name("textarea").send_keys(answer)
    browser.find_element_by_css_selector("button.submit-submission").click()
    text = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    assert text == "Correct!", text
