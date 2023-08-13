from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import TIMEOUT
from locators import Locator
from utilities import Generator


def registration(driver: ChromiumDriver) -> tuple[str, str]:
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
    WebDriverWait(driver, TIMEOUT).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, Locator.header_authorization)
        )
    )
    driver.find_element(By.XPATH, Locator.logo).click()
    WebDriverWait(driver, TIMEOUT).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, Locator.btn_login_main)
        )
    )
    return (email, password)


def authorization(driver: ChromiumDriver, email: str, password: str) -> None:
    driver.find_element(By.XPATH, Locator.btn_login_main).click()
    driver.find_element(By.XPATH, Locator.input_email).send_keys(email)
    driver.find_element(By.XPATH, Locator.input_password).send_keys(password)
    driver.find_element(By.XPATH, Locator.btn_login).click()
    WebDriverWait(driver, TIMEOUT).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, Locator.btn_checkout)
        )
    )
