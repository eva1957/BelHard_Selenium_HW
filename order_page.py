import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from const import FIND_TIMEOUT
from main_page import BasePage


class MakeOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_url_order_page(self, result):
        card_url = self.driver.current_url
        assert card_url == result
        print("URL Order Page is correct")

    # Locators
    current_url = "https://boomkids.by/cart"
    coupon_field = "//input[@id='coupon']"
    button_coupon = "//div[@id='btnCoupon']"
    checkbox_no_confirm = "//label[@for='cartPersonNoConfirm']"

    # Getters
    def get_coupon(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.coupon_field)))

    def get_button_coupon(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.button_coupon)))

    def get_checkbox(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_no_confirm)))

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

    # Methods
    def continue_order(self):
        self.assert_url_order_page(self.current_url)
        self.input_coupon()
        self.click_button_coupon()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.click_checkbox()


class ChooseDeliveryAndPayment(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    radiobutton_delivery = "//label[@for='deliveryMethodDPD.courierNoContact']"
    radiobutton_halva = "//label[@for='paymentMethodHalva']"

    # Getters
    def get_radiobutton_delivery(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_delivery)))

    def get_radiobutton_halva(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_halva)))

    # Actions
    def click_radiobutton_delivery(self):
        self.get_radiobutton_delivery().click()
        print("Click radiobutton DPD delivery")

    def click_radiobutton_halva(self):
        self.get_radiobutton_halva().click()
        print("Click radiobutton Halva")

    # Methods
    def delivery_and_payment(self):
        self.click_radiobutton_delivery()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.click_radiobutton_halva()
        self.driver.execute_script("window.scrollTo(0,500)")