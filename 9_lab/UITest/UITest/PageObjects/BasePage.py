from tests.conf import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    def __init__(self, driver):
        options = Options()
        options.add_argument("--lang=ru")
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.get(SITE_URL)
        else:
            self._driver = driver
