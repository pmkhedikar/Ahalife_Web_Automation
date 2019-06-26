from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import unittest


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver: WebDriver = webdriver.Chrome(
            executable_path="D:\Ahalife_Web_Automation\drivers\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("https://wwwqa.designmilktravels.com")
        self.driver.find_element_by_xpath("//*[@class='mc-closeModal']").click()
        self.driver.find_element_by_xpath("//*[@class='sign_in']").click()
        self.driver.find_element_by_xpath("//*[@id='loginUsername']").send_keys('international@dispostable.com')
        self.driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys('pass@12345678')
        self.driver.find_element_by_xpath("//*[@type='submit' and @value='Sign In']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



   #def test_invald_login(self):




