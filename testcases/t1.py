import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

#driver =webdriver.Chrome()


class Test(unittest):
    def test_first(self):
        driver.WebDriver = webdriver.Chrome(executable_path="D:\Ahalife_Web_Automation\drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://wwwqa.designmilktravels.com")
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//*[@class='mc-closeModal']").click()
    if __name__=="__main__":
        unittest.main()

