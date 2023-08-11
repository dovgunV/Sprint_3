import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from locators import Locator
from utilities import Generator

_BASE = "https://stellarburgers.nomoreparties.site/"
_TIMEOUT: float = 2


@pytest.fixture
def driver() -> ChromiumDriver:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(
        options, Service(ChromeDriverManager().install())
    )
    browser.get(_BASE)
    return browser


@pytest.fixture
def registered(driver: ChromiumDriver) -> tuple[ChromiumDriver, str, str]:
    driver.find_element(By.XPATH, Locator.btn_personal_account).click()
    driver.find_element(
        By.XPATH, Locator.btn_registration_for_authorization
    ).click()
    driver.find_element(By.XPATH, Locator.input_name).send_keys(
        Generator.login()
    )
    email, password = Generator.email(), Generator.password()
    driver.find_element(By.XPATH, Locator.input_email).send_keys(email)
    driver.find_element(By.XPATH, Locator.input_password).send_keys(password)
    driver.find_element(By.XPATH, Locator.btn_register).click()
    WebDriverWait(driver, _TIMEOUT).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, Locator.header_authorization)
        )
    )
    driver.find_element(By.XPATH, Locator.logo).click()
    WebDriverWait(driver, _TIMEOUT).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, Locator.btn_login_main)
        )
    )
    return (driver, email, password)


@pytest.fixture
def authorized(registered: tuple[ChromiumDriver, str, str]) -> ChromiumDriver:
    driver, email, password = registered
    driver.find_element(By.XPATH, Locator.btn_login_main).click()
    driver.find_element(By.XPATH, Locator.input_email).send_keys(email)
    driver.find_element(By.XPATH, Locator.input_password).send_keys(password)
    driver.find_element(By.XPATH, Locator.btn_login).click()
    WebDriverWait(driver, _TIMEOUT).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, Locator.btn_checkout)
        )
    )
    return driver
