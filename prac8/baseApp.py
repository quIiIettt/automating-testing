from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseApp:
    def __init__(self, browser):
        self.browser = browser
        self.link = "https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html"

    def go_to_site(self):
        self.browser.get(self.link)

    def find_element(self, value, timeout=10):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((value))
            )
            return element
        except Exception as e:
            print(f"Element with ID '{value}' not found: {e}")