from LocatorList.locator import *
import time
import configparser

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        driver.implicitly_wait(15)

class MainPage(BasePage):
    def LoginApp(self):
        element_icon_login = self.driver.find_element(*MainPageLocators.ICON_LOGIN)
        element_icon_login.click()
        time.sleep(3)
        element_login = self.driver.find_element(*MainPageLocators.LOGIN)
        element_login.click()
        time.sleep(3)

        """
        This method logs into the application using the username and password specified in the credential.ini file.
        """
        config = configparser.ConfigParser()
        config.read('credential.ini')
        username = config.get("application", "username")
        password = config.get("application", "password")

        element_username = self.driver.find_element(*MainPageLocators.MEDIA_ID)
        element_username.send_keys(username)
        element_password = self.driver.find_element(*MainPageLocators.PASSWORD)
        element_password.send_keys(password)
        element_btn_login = self.driver.find_element(*MainPageLocators.BTN_LOGIN)
        element_btn_login.click()
        time.sleep(5)

assert 'MainPage' in globals(), 'MainPage class not found'
assert 'LoginApp' in dir(MainPage), 'LoginApp method not found in MainPage class'
assert '__init__' in dir(BasePage), '__init__ method not found in BasePage class'

