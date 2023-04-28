from LocatorList.locator import *
from selenium.webdriver.common.keys import Keys
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(15)


class MainPage(BasePage):
    def SearchContent(self):
        element_search = self.driver.find_element(*MainPageLocators.SEARCH)
        element_search.send_keys("Berita IT" + Keys.RETURN)
        time.sleep(3)
        search_results = self.driver.find_element(*MainPageLocators.SEARCH_RESULTS)
        assert "BERITA IT" in search_results.text.upper(), "Search results do not contain expected text."
