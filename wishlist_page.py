from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from const import FIND_TIMEOUT
from main_page import BasePage


class AddToWishlist(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_add_tolist = "//div[@class='btn btn-magenta bg-white color-magenta rounded d-inline-block text-center my-2 link-wishlist icons icons-heart icons-mr-2 flex-grow-1']"

    # Getters
    def get_button_add(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.button_add_tolist)))

    # Actions
    def click_button_add_to_wl(self):
        self.get_button_add().click()
        print("Click button add to wishlist")

    # Methods
    def add_to_wl(self):
        self.click_button_add_to_wl()


class Wishlist(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    icon_wishlist = "//a[@href='/myaccount/wishlist']"
    icon_basket = "//span[@class='icons icons-basket-huge']"

    # Getters
    def get_wishlist(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.icon_wishlist)))

    def get_basket(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.icon_basket)))

    # Actions
    def click_wishlist(self):
        self.get_wishlist().click()
        print("Click wishlist")

    def click_basket(self):
        self.get_basket().click()
        print("Click basket")

    # Methods
    def wishlist_and_basket(self):
        self.click_wishlist()
        self.click_basket()

