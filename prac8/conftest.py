import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 800)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()