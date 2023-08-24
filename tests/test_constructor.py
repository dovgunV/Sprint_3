from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import TIMEOUT
from helpers import authorization, registration
from locators import Locator


class TestConstructor:
    def test_constructor_transition_fillings_correct(
        self, driver: ChromiumDriver
    ) -> None:
        authorization(driver, *registration(driver))
        driver.find_element(By.XPATH, Locator.btn_fillings).click()
        header = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_fillings)
                )
            )
            .text
        )
        assert header == "Начинки"

    def test_constructor_transition_rolls_correct(
        self, driver: ChromiumDriver
    ) -> None:
        authorization(driver, *registration(driver))
        driver.find_element(By.XPATH, Locator.btn_fillings).click()
        WebDriverWait(driver, TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locator.header_fillings)
            )
        )
        driver.find_element(By.XPATH, Locator.btn_rolls).click()
        header = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_rolls)
                )
            )
            .text
        )
        assert header == "Булки"

    def test_constructor_transition_sauces_correct(
        self, driver: ChromiumDriver
    ) -> None:
        authorization(driver, *registration(driver))
        driver.find_element(By.XPATH, Locator.btn_sauces).click()
        header = (
            WebDriverWait(driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_sauces)
                )
            )
            .text
        )
        assert header == "Соусы"
