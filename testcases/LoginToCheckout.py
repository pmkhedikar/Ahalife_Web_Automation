from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

#driver =webdriver.Chrome()

driver: WebDriver = webdriver.Chrome(executable_path="D:\Ahalife_Web_Automation\drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://wwwqa.designmilktravels.com")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@class='mc-closeModal']").click()
driver.find_element_by_xpath("//*[@class='sign_in']").click()
driver.find_element_by_xpath("//*[@id='loginUsername']").send_keys('international@dispostable.com')
driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys('pass@12345678')
driver.find_element_by_xpath("//*[@type='submit' and @value='Sign In']").click()

#Account Setting
driver.find_element_by_xpath("//*[@class='account ']").click()

#Search
driver.find_element_by_xpath("//*[@class='desktop-search-input']").click()
driver.find_element_by_xpath("//*[@class='desktop-search-input']").send_keys('Bag')
driver.find_element_by_xpath("//*[@class='desktop-search-input']").send_keys(Keys.RETURN)
driver.find_element_by_xpath("//*[@class='product-image-container-overlay']").click()
driver.implicitly_wait(2)


#PDP Page ,My Bag ,Paymennt & Place Order
driver.find_element_by_xpath("//*[@id='buy-button']").click()
driver.find_element_by_xpath("//*[@href='/bag']").click()
driver.find_element_by_xpath("//*[@value='Begin Checkout']").click()
driver.find_element_by_xpath("//*[@value='PLACE ORDER']").click()
driver.find_element_by_xpath("//*[text()='Order # ']//a").click()
driver.close()


