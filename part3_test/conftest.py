import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language, for example: ru or es or fr")


@pytest.fixture(scope="function")
def browser(request):
    # de-DE
    browser_language = request.config.getoption("language")
    print("\nstart browser for test..", browser_language)
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    option.add_argument(f"--lang={browser_language}")
    browser = webdriver.Chrome(options=option)
    yield browser
    print("\nquit browser..")
    browser.quit()
