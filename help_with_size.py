from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from const import FIND_TIMEOUT
from main_page import BasePage


class HelpWithSize(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    link_need_help = "//a[@href='#caMB-size']"
    header_mothercare = "//div[@id='heading1']"
    header_kids_clothes = "//div[@id='mothercare-4']"
    button_close = "//button[@type='submit']"

    # Getters
    def get_link_need_help(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.link_need_help)))

    def get_header_mothercare(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.header_mothercare)))

    def get_header_kids_clothes(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.header_kids_clothes)))

    def get_button_close(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.button_close)))

    # Actions

    def click_link_help(self):
        self.get_link_need_help().click()
        print("Click link help")

    def click_header_mothercare(self):
        self.get_header_mothercare().click()
        print("Click header mothetcare")

    def click_header_kids_clothes(self):
        self.get_header_kids_clothes().click()
        print("Click header kids clothes")

    def click_button_close(self):
        self.get_button_close().click()
        print("Click button close")

    # Methods
    def help_with_size(self):
        self.click_link_help()
        self.click_header_mothercare()
        self.click_header_kids_clothes()
        self.click_button_close()
