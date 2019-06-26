from selenium.common.exceptions import NoSuchElementException
class LoginPage():

    #Creating the constructor
    def __init__(self, driver):
        self.driver = driver

    # Defining locators on that page
        self.mailchimpPopup_closeIcon = "//*[@class='mc-closeModal']"
        self.signin_link_xpath = "//*[@class='sign_in']"
        self.username_textbox_xpath = "//*[@id='loginUsername']"
        self.password_textbox_xpath = "//*[@id='loginPassword']"
        self.signin_button_xpath = "//*[@type='submit' and @value='Sign In']"
        self.login_error_message = "//*[@class='auth-errors' and text()='The e-mail address and/or password entered do not match our records.  Please try again.']"

    # Defining the Method to perform operations on those elements

    def mailchimp_popup_close(self):
        self.driver.find_element_by_xpath(self.mailchimpPopup_closeIcon).click()


    def sing_in(self):
        self.driver.find_element_by_xpath(self.signin_link_xpath).click()


    def enter_username(self, username):
        #self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)


    def enter_password(self, password):
        #self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)


    def click_login(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()


    def check_invalid_login_message(self):
        try:
            webdriver.find_element_by_xpath(self.login_error_message)
        except NoSuchElementException:
            return False
        return True


        #msg = self.driver.find_element_by_xpath(self.login_error_message).text
        #return msg




