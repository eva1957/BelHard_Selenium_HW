from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from const import FIND_TIMEOUT
from main_page import BasePage


class PersonalInfo(BasePage):
    # Locators
    field_name = "//input[@id='cartPersonFirstName']"
    field_last_name = "//input[@id='cartPersonLastName']"
    field_phone = "//input[@id='cartPersonPhone']"
    email = "//input[@id='cartPersonEmail']"
    checkbox_subscription = "//label[@for='cartPersonSubscribeNews']"

    # Getters
    def get_field_name(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.field_name)))

    def get_field_last_name(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.field_last_name)))

    def get_field_phone(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.field_phone)))

    def get_email(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_checkbox(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_subscription)))

    # Actions
    def input_name(self):
        self.get_field_name().send_keys("Юлия")
        print("Input name")

    def input_last_name(self):
        self.get_field_last_name().send_keys("Романчук")
        print("Input last name")

    def input_phone(self):
        self.get_field_phone().send_keys(123456789)
        print("Input phone")

    def input_email(self):
        self.get_email().send_keys('123@mail.ru')
        print("Input email")

    def click_checkbox(self):
        self.get_checkbox().click()
        print("Click checkbox subscription and driver closed")

    # Methods
    def complete_order(self):
        self.input_name()
        self.input_last_name()
        self.input_phone()
        self.input_email()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.click_checkbox()
        self.driver.close()




