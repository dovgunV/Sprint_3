from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import TIMEOUT
from helpers import authorization, registration
from locators import Locator


class TestPersonalAccount:
    def test_personal_account_transition_successful(
        self, driver: ChromiumDriver
    ) -> None:
        authorization(driver, *registration(driver))
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        button_text = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.btn_exit)
                )
            )
            .text
        )
        assert button_text == "Выход"

    def test_personal_account_logout_user_logged_out(
        self, driver: ChromiumDriver
    ) -> None:
        authorization(driver, *registration(driver))
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        WebDriverWait(driver, TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locator.btn_exit)
            )
        ).click()
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

    def test_personal_account_transition_constructor_through_button_successful(
        self, driver: ChromiumDriver
    ) -> None:
        authorization(driver, *registration(driver))
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(By.XPATH, Locator.btn_constructor).click()
        header = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_main)
                )
            )
            .text
        )
        assert header == "Соберите бургер"

    def test_personal_account_transition_constructor_through_logo_successful(
        self, driver: ChromiumDriver
    ) -> None:
        authorization(driver, *registration(driver))
        driver.find_element(By.XPATH, Locator.btn_personal_account).click()
        driver.find_element(By.XPATH, Locator.logo).click()
        header = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_main)
                )
            )
            .text
        )
        assert header == "Соберите бургер"
