from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import TIMEOUT
from locators import Locator
from utilities import Generator


class TestRegister:
    def test_register_successfully_registered(
        self, driver: ChromiumDriver
    ) -> None:
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(
            By.XPATH, Locator.btn_registration_for_authorization
        ).click()
        driver.find_element(By.XPATH, Locator.input_name).send_keys(
            Generator.login()
        )
        driver.find_element(By.XPATH, Locator.input_email).send_keys(
            Generator.email()
        )
        driver.find_element(By.XPATH, Locator.input_password).send_keys(
            Generator.password()
        )
        driver.find_element(By.XPATH, Locator.btn_register).click()
        header = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_authorization)
                )
            )
            .text
        )
        assert header == "Вход"

    def test_register_incorrect_password_not_registered(
        self, driver: ChromiumDriver
    ) -> None:
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(
            By.XPATH, Locator.btn_registration_for_authorization
        ).click()
        driver.find_element(By.XPATH, Locator.input_name).send_keys(
            Generator.login()
        )
        driver.find_element(By.XPATH, Locator.input_email).send_keys(
            Generator.email()
        )
        driver.find_element(By.XPATH, Locator.input_password).send_keys(
            Generator.password(2)
        )
        driver.find_element(By.XPATH, Locator.btn_register).click()
        message = (
            WebDriverWait(driver, 3)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.message_incorrect_password)
                )
            )
            .text
        )
        assert message == "Некорректный пароль"

    def test_register_empty_name_not_registered(
        self, driver: ChromiumDriver
    ) -> None:
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(
            By.XPATH, Locator.btn_registration_for_authorization
        ).click()
        driver.find_element(By.XPATH, Locator.input_email).send_keys(
            Generator.email()
        )
        driver.find_element(By.XPATH, Locator.input_password).send_keys(
            Generator.password()
        )
        driver.find_element(By.XPATH, Locator.btn_register).click()
        header = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_registration)
                )
            )
            .text
        )
        assert header == "Регистрация"
