
class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.accountsetting_link_xpath = "//*[@href='/account']"
        self.signout_link_xpath = "//*[@class='account ']//ul//li[5]//a"


    def click_accountsetting(self):
        self.driver.find_element_by_xpath(self.accountsetting_link_xpath).click()

    def signout(self):
        self.driver.find_element_by_xpath(self.signout_link_xpath).click()





