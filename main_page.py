from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from const import FIND_TIMEOUT


class BasePage:
    def __init__(self, driver: Firefox):
        self.driver = driver

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")


class LoginPage(BasePage):

    # Locators
    url = "https://boomkids.by/"
    button_accept_cookie = "//button[@class='btn btn-green']"

    def get_url(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.url)))

    def get_cookie(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.button_accept_cookie)))

    # Actions
    def open_url(self):
        self.get_url().click()
        print("Open site")

    def click_cookie(self):
        self.get_cookie().click()
        print("Click Cookie")

    # Methods
    def go_to_site(self):
        self.driver.get(self.url)
        self.assert_url(self.url)
        self.click_cookie()


class Filters(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    tab_for_girl = "//a[@id='mainmenu2']"
    link_mothercare = "//a[@data-fval='Mothercare']"

    # Getters
    def get_tab_for_girl(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.tab_for_girl)))

    def get_link_mothercare(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.link_mothercare)))

    # Actions
    def click_tab(self):
        self.get_tab_for_girl().click()
        print("Click Tab for girl")

    def click_link(self):
        self.get_link_mothercare().click()
        print("Click Tab for girl")

    def select_filters(self):
        self.click_tab()
        self.click_link()


class DropdownMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    dropdown_menu = "//a[@href='/girls/verhnyaya-odezhda?f.brand=Mothercare']"
    filter_coat = "#filterCat1 > div:nth-child(3) > a:nth-child(1) > div:nth-child(1)"
    link_coat = "//div[@data-sku='LFB630']"

    # Getters
    def get_dropdown_menu(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_menu)))

    def get_filter_coat(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_coat)))

    def get_link_coat(self, timeout=FIND_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, self.link_coat)))

    # Actions
    def click_dropdown_menu(self):
        self.get_dropdown_menu().click()
        print("Click dropdown menu")

    def click_filter_coat(self):
        self.get_filter_coat().click()
        print("Click Filter coat")

    def click_link_coat(self):
        self.get_link_coat().click()
        print("Click Link coat")

    # Methods
    def select_clothes(self):
        self.click_dropdown_menu()
        self.click_filter_coat()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.click_link_coat()
