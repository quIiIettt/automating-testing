import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://testpages.eviltester.com/styled/index.html"
browser = driver = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)

#test 1
browser.find_element(By.XPATH, "//a[contains(text(),'Dynamic Buttons Challenge 02')]").click()
time.sleep(3)

#test 2
start_button = browser.find_element(by=By.ID, value='button00')
start_button.click()
time.sleep(3)

#test 3
one_button = browser.find_element(by=By.ID, value='button01')
one_button.click()
time.sleep(3)

#test 4
two_button = browser.find_element(by=By.ID, value='button02')
two_button.click()
time.sleep(3)

#test 5
assert browser.find_element(by=By.ID, value='button02').is_displayed()