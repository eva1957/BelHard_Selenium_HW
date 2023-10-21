import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='session')
def driver():
    manager = GeckoDriverManager()
    service = Service(manager.install())
    driver = Firefox(service=service)
    driver.implicitly_wait(1)
    return driver



