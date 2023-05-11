import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from TestCases import test_login, test_search
import HTMLRunner.HTMLTestRunner as HTMLTestRunner


class PythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.kompas.com/")
        self.driver.maximize_window()
        time.sleep(3)

    def test1_login(self):
        mainPage = test_login.MainPage(self.driver)
        mainPage.LoginApp()
        print("Test Login Passed")

    def test2_searchContent(self):
        mainPage = test_login.MainPage(self.driver)
        mainPage.LoginApp()
        mainPage = test_search.MainPage(self.driver)
        mainPage.SearchContent()
        print("test search Passed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        # print("Test Completed")

if __name__ == "__main__":
    with open('report.html', 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='Test Report',
            description='Test Report'
        )
        unittest.main(testRunner=runner)