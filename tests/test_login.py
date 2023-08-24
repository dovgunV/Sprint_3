from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import TIMEOUT
from helpers import registration
from locators import Locator


class TestLogin:
    def test_login_from_home_page_authorization_passed(
        self, driver: ChromiumDriver
    ) -> None:
        email, password = registration(driver)
        driver.find_element(By.XPATH, Locator.btn_login_main).click()
        driver.find_element(By.XPATH, Locator.input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.input_password).send_keys(
            password
        )
        driver.find_element(By.XPATH, Locator.btn_login).click()
        button_text = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.btn_checkout)
                )
            )
            .text
        )
        assert button_text == "Оформить заказ"

    def test_login_through_personal_account_authorization_passed(
        self, driver: ChromiumDriver
    ) -> None:
        email, password = registration(driver)
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(By.XPATH, Locator.input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.input_password).send_keys(
            password
        )
        driver.find_element(By.XPATH, Locator.btn_login).click()
        button_text = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.btn_checkout)
                )
            )
            .text
        )
        assert button_text == "Оформить заказ"

    def test_login_through_registration_authorization_passed(
        self, driver: ChromiumDriver
    ) -> None:
        email, password = registration(driver)
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(
            By.XPATH, Locator.btn_registration_for_authorization
        ).click()
        driver.find_element(By.XPATH, Locator.btn_login_register).click()
        driver.find_element(By.XPATH, Locator.input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.input_password).send_keys(
            password
        )
        driver.find_element(By.XPATH, Locator.btn_login).click()
        button_text = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.btn_checkout)
                )
            )
            .text
        )
        assert button_text == "Оформить заказ"

    def test_login_through_recovery_authorization_passed(
        self, driver: ChromiumDriver
    ):
        email, password = registration(driver)
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(By.XPATH, Locator.btn_restore_password).click()
        driver.find_element(
            By.XPATH, Locator.btn_login_restore_password
        ).click()
        driver.find_element(By.XPATH, Locator.input_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.input_password).send_keys(
            password
        )
        driver.find_element(By.XPATH, Locator.btn_login).click()
        button_text = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.btn_checkout)
                )
            )
            .text
        )
        assert button_text == "Оформить заказ"
