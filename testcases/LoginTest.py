from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver: WebDriver = webdriver.Chrome(
            executable_path="D:\Ahalife_Web_Automation\drivers\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test01_valid_login(self):
        driver = self.driver
        driver.get("https://wwwqa.designmilktravels.com")

        login = LoginPage(driver)

        login.mailchimp_popup_close()
        login.sing_in()
        login.enter_username("international@dispostable.com")
        login.enter_password("pass@12345678")
        login.click_login()


        homepage = HomePage(driver)

        homepage.click_accountsetting()
        #homepage.signout()

    def test02_invalid_login(self):
        driver = self.driver
        driver.get("https://www.designmilktravels.com")

        login = LoginPage(driver)

        login.mailchimp_popup_close()
        login.sing_in()
        login.enter_username("invalid_id@dispostable.com")
        login.enter_password("pass@12345678")
        login.click_login()
        driver.implicitly_wait(10)
        login.login_error_message()
        #message = driver.find_element_by_xpath("").text
        #self.assertEqual(message ," The e-mail address and/or password entered do not match our records.  Please try again.")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

    # def test_invald_login(self):

# self.driver.find_element_by_xpath("//*[@class='mc-closeModal']").click()
# self.driver.find_element_by_xpath("//*[@class='sign_in']").click()
# self.driver.find_element_by_xpath("//*[@id='loginUsername']").send_keys('international@dispostable.com')
# self.driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys('pass@12345678')
# self.driver.find_element_by_xpath("//*[@type='submit' and @value='Sign In']").click()
