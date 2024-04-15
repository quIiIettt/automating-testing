from selenium import webdriver
from baseApp import BaseApp
from dynamicButtonsPages import DynamicButtonsLocator, SearchHelper
from selenium.webdriver.common.by import By
import pytest
import time

class TestsDynamicButtons:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.base_app = BaseApp(webdriver.Chrome())
        yield
        self.base_app.browser.quit()

    def test_click_buttons_and_verify_text(self):
        self.base_app.go_to_site()
        search_helper = SearchHelper(self.base_app)

        # search_helper.click_button_1()
        # search_helper.click_button_2()
        # search_helper.click_button_3()
        # search_helper.click_button_4()

        # text = search_helper.get_all_buttons_clicked_text()
        # assert text == "All Buttons Clicked"

        self.base_app.find_element((By.ID, 'button00')).click()
        time.sleep(3)
        self.base_app.find_element((By.ID, 'button01')).click()
        time.sleep(3)
        self.base_app.find_element((By.ID, 'button02')).click()
        time.sleep(3)
        self.base_app.find_element((By.ID, 'button03')).click()
        time.sleep(3)