import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from const import FIND_TIMEOUT
from main_page import BasePage


class MakeOrder(BasePage):
    # Locators
    coupon_field = "//input[@id='coupon']"
    button_coupon = "//div[@id='btnCoupon']"
    checkbox_no_confirm = "//label[@for='cartPersonNoConfirm']"
    radiobutton_delivery = "//label[@for='deliveryMethodDPD.courierNoContact']"
    radiobutton_halva = "//label[@for='paymentMethodHalva']"

    # Getters
    def get_coupon(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.coupon_field)))

    def get_button_coupon(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.button_coupon)))

    def get_checkbox(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_no_confirm)))

    def get_radiobutton_delivery(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_delivery)))

    def get_radiobutton_halva(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_halva)))

    # Actions
    def input_coupon(self):
        self.get_coupon().send_keys("bonus15")
        print("Input coupon")

    def click_button_coupon(self):
        self.get_button_coupon().click()
        print("Click button coupon")
        time.sleep(2)

    def click_checkbox(self):
        self.get_checkbox().click()
        print("Click checkbox no confirm")

    def click_radiobutton_delivery(self):
        self.get_radiobutton_delivery().click()
        print("Click radiobutton DPD delivery")

    def click_radiobutton_halva(self):
        self.get_radiobutton_halva().click()
        print("Click radiobutton Halva")

    # Methods
    def continue_order(self):
        self.input_coupon()
        self.click_button_coupon()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.click_checkbox()
        self.click_radiobutton_delivery()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.click_radiobutton_halva()
        self.driver.execute_script("window.scrollTo(0,500)")



