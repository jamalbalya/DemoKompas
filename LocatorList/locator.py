from selenium.webdriver.common.by import By

class MainPageLocators(object):
    ICON_LOGIN = (By.ID, "sso__icon__login_top")
    LOGIN = (By.ID, "txt_signin")
    MEDIA_ID = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[3]/input")

    SEARCH = (By.ID, "search")
    SEARCH_RESULTS = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div")