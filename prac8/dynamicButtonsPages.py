from selenium.webdriver.common.by import By
from baseApp import BaseApp

class DynamicButtonsLocator:
    START_button = (By.ID, 'button00')
    ONE_button = (By.ID, 'button01')
    TWO_button = (By.ID, 'button02')
    THREE_button = (By.ID, 'button03')
    ALL_BUTTONS_CLICKED_TEXT = (By.ID, 'buttonmessage')

class SearchHelper:
    def __init__(self, browser):
        self.browser = browser
        self.base_app = BaseApp(browser)

    def click_button_1(self):
        self.base_app.find_element(DynamicButtonsLocator.START_button).click()
        
    def click_button_2(self):
        self.base_app.find_element(DynamicButtonsLocator.ONE_button).click()

    def click_button_3(self):
        self.base_app.find_element(DynamicButtonsLocator.TWO_button).click()

    def click_button_4(self):
        self.base_app.find_element(DynamicButtonsLocator.THREE_button).click()

    def get_all_buttons_clicked_text(self):
        return self.base_app.find_element(*DynamicButtonsLocator.ALL_BUTTONS_CLICKED_TEXT).text