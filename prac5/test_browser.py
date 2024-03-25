import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test1(browser):
    link = "https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=20"
    browser.get(link)
    browser.find_element(By.XPATH, "//a[contains(text(),'Phones & PDAs (3)')]").click()
    assert "Phones & PDAs" in browser.title

def test2(browser):
    link = "https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=20"
    browser.get(link)
    browser.find_element(By.XPATH, "//a[contains(text(),'Phones & PDAs (3)')]").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'iPhone')]").click()

def test3(browser):
    link = "https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=20"
    browser.get(link)
    browser.find_element(By.XPATH, "//a[contains(text(),'Phones & PDAs (3)')]").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'iPhone')]").click()
    assert browser.find_element(By.XPATH, "//li[contains(text(),'Product Code: product 11')]").is_displayed()
