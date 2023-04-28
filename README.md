This codebase contains Python scripts that perform automated testing using Selenium WebDriver on the website Kompas.com. 
The main.py script is the entry point that runs the test cases for logging in and searching for content on the website. 
The script imports test_login.py and test_search.py, which contain the implementation for the test cases.

The script starts by setting up the Chrome WebDriver using the ChromeDriverManager package and navigates to 
the Kompas.com website. It then runs the test cases for logging in and searching for content on the website using the 
unittest module.

1. The MainPage class extends the BasePage class and defines a LoginApp() method that logs into the application using 
   the username and password specified in the credential.ini file.
2. The test_login.py script contains the implementation for logging in to the website. It initializes the BasePage class, 
   which has a constructor that takes in the WebDriver object and sets an implicit wait time.
3. The test_search.py script contains the implementation for searching for content on the website. 
   It initializes the BasePage class and defines a SearchContent() method that searches for the specified content on 
   the website and verifies that the search results contain the expected text.
4. The locator.py script contains the definition of the locators used in the MainPage class of test_login.py and 
   test_search.py. It uses the By module from Selenium WebDriver to define the locators.
   When the test cases are run (on main.py or using terminal python3 main.py), a HTML report is generated using 
   the HTMLTestRunner package, which shows the status of each test case and any errors that occurred during the test. 
   The report.html file is generated in the same directory as the main.py script.