from typing import Tuple

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from const import FIND_TIMEOUT


class Locators:
    button_accept_cookie = (By.XPATH, "//button[@class='btn btn-green']")
    tab_for_girl = (By.XPATH, "//a[@id='mainmenu2']")
    link_mothercare = (By.XPATH, "//a[@data-fval='Mothercare']")


class BasePage:
    def __init__(self, driver: Firefox):
        self.driver = driver

    def find_element(self, locator: Tuple[str], timeout=FIND_TIMEOUT):
        conditions = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(conditions)

    def is_exist(self, locator: Tuple[str], timeout=FIND_TIMEOUT):
        try:
            self.driver.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def click_to_element(self, locator, timeout=FIND_TIMEOUT):
        element = self.find_element(locator, timeout)
        element.click()
        return element


class Clothes(BasePage):
    pass
