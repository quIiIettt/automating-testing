import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def get_url(browser): 
    link = "https://testpages.eviltester.com/styled/index.html"
    browser.get(link)
    browser.find_element(By.XPATH, "//a[contains(text(),'Dynamic Buttons Challenge 01')]").click()

def test_timeSleep(browser):
    get_url(browser)
    start_button = browser.find_element(by=By.ID, value='button00')
    start_button.click()
    one_button = browser.find_element(by=By.ID, value='button01')
    one_button.click()
    time.sleep(3)
    two_button = browser.find_element(by=By.ID, value='button02')
    two_button.click()
    assert browser.find_element(by=By.ID, value='button02').is_displayed() 

def test_webDriverWait(browser):
    get_url(browser)
    start_button = browser.find_element(by=By.ID, value='button00')
    start_button.click()
    one_button = browser.find_element(by=By.ID, value='button01')
    one_button.click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'button02')))
    two_button = browser.find_element(by=By.ID, value='button02')
    two_button.click()
    assert browser.find_element(by=By.ID, value='button02').is_displayed()

def test_implicitlyWait(browser):
    get_url(browser)
    start_button = browser.find_element(by=By.ID, value='button00')
    start_button.click()
    one_button = browser.find_element(by=By.ID, value='button01')
    one_button.click()
    browser.implicitly_wait(10)
    two_button = browser.find_element(by=By.ID, value='button02')
    two_button.click()
    assert browser.find_element(by=By.ID, value='button02').is_displayed()