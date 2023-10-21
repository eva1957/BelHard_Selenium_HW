import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from const import FIND_TIMEOUT
from main_page import BasePage


class CoatPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_coat_size = "//option[@value='201177']"
    button_buy = "//button[@class='btn btn-orange color-white w-100 link-add-to-cart my-2']"

    # Getters
    def get_select_size(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.select_coat_size)))

    def get_button_buy(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    # Actions
    def click_select_size(self):
        self.get_select_size().click()
        print("Select size")

    def click_button_buy(self):
        self.get_button_buy().click()
        print("Click button buy")
        time.sleep(2)

    # Methods
    def select_size(self):
        self.click_select_size()
        self.click_button_buy()



