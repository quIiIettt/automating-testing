import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

link = "https://testpages.eviltester.com/styled/index.html"
browser = driver = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)

browser.find_element(By.XPATH, "//a[contains(text(),'HTML Form Example')]").click()
time.sleep(2)

#1 test
username = browser.find_element(By.NAME, "username")
username.send_keys("user123")
time.sleep(2)

password = browser.find_element(By.NAME, "password")
password.send_keys("password123")
time.sleep(2)

comments = browser.find_element(By.NAME, "comments")
comments.send_keys("MY APPLE!")
time.sleep(2)

file_path = "C:\\Users\\cooyy\\OneDrive\\Desktop\\TA\\test1.txt"
file_upload_element = browser.find_element(By.NAME, "filename")
file_upload_element.send_keys(file_path)
time.sleep(2)

checkboxes = browser.find_elements(By.CSS_SELECTOR, "input[name='checkboxes[]']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") in ("cb1", "cb3"):
        checkbox.click()

time.sleep(2)

radio_button = browser.find_element(By.CSS_SELECTOR, "input[name='radioval'][value='rd2']")
radio_button.click()

time.sleep(2)

multiselect = Select(browser.find_element(By.NAME, "multipleselect[]"))
multiselect.select_by_value("ms1")

time.sleep(2)

dropdown = Select(browser.find_element(By.NAME, "dropdown"))
dropdown.select_by_value("dd4")

time.sleep(2)

submit_button = browser.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()

time.sleep(3)

#2 test auth
browser.get(link)
browser.find_element(By.XPATH, "//a[contains(text(),'Basic Authentication Protected Page')]").click()

username_element = browser.find_element(By.XPATH, "//p[contains(text(),'username:')]")
password_element = browser.find_element(By.XPATH, "//p[contains(text(),'password:')]")

time.sleep(2)

auth_username = username_element.text.split(":")[-1].strip()
auth_password = password_element.text.split(":")[-1].strip()

browser.find_element(By.XPATH, "//a[contains(text(),'Basic Auth Protected Page')]").click()

time.sleep(1)

pyautogui.write("authorized")
pyautogui.press("tab")

time.sleep(1)

pyautogui.write("password001")

time.sleep(1)

pyautogui.press("enter")

time.sleep(2)

#3 test upload file
browser.get(link)
browser.find_element(By.XPATH, "//a[contains(text(),'File Upload Example Page')]").click()

time.sleep(2)


file_path = "C:\\Users\\cooyy\\OneDrive\\Desktop\\TA\\test1.txt"
file_upload_element = browser.find_element(By.NAME, "filename")
file_upload_element.send_keys(file_path)

time.sleep(2)

file_button = browser.find_element(By.CSS_SELECTOR, "input[name='filetype'][value='text']")
file_button.click()

upload_button = browser.find_element(By.NAME, "upload")
upload_button.click()

time.sleep(2)

assert browser.find_element(By.XPATH, "//p[contains(text(),'You uploaded a file. This is the result.')]").is_displayed()

time.sleep(2)

#4 test alert
browser.get(link)
browser.find_element(By.XPATH, "//a[contains(text(),'Alerts (JavaScript)')]").click()

time.sleep(2)

button = browser.find_element(by=By.ID, value='confirmexample')
button.click()

try:
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    text = alert.text
    time.sleep(2)
    print(f"Alert text: {text}")
    alert.accept()
    time.sleep(2) 

except (TimeoutException, NoAlertPresentException) as e:
    print(f"Error: {e}")

browser.quit()