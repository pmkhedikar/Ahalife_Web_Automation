from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


#driver =webdriver.Chrome()

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="D:\Ahalife_Web_Automation\drivers\chromedriver_win32\chromedriver.exe")
    driver.get("https://wwwqa.designmilktravels.com")
    driver.maximize_window()
    driver.implicitly_wait(2)


def test_login():
    driver.find_element_by_xpath("//*[@class='mc-closeModal']").click()
    driver.find_element_by_xpath("//*[@class='sign_in']").click()
    driver.find_element_by_xpath("//*[@id='loginUsername']").send_keys('international@dispostable.com')
    driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys('pass@12345678')
    driver.find_element_by_xpath("//*[@type='submit' and @value='Sign In']").click()
    driver.find_element_by_xpath("//*[@class='account ']").click()
    driver.implicitly_wait(10)
    x = driver.title
    assert x == "abc"


def test_teardown():
    driver.close()
    driver.quit()
    print('Test completed')