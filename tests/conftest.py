import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait




@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get('https://qa-scooter.praktikum-services.ru/')
    yield browser
    browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
