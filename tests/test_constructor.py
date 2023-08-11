from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestConstructor:
    _TIMEOUT: float = 2

    def test_constructor_transition_fillings_correct(
        self, authorized: ChromiumDriver
    ) -> None:
        authorized.find_element(By.XPATH, Locator.btn_fillings).click()
        header = (
            WebDriverWait(authorized, self._TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_fillings)
                )
            )
            .text
        )
        authorized.quit()
        assert header == "Начинки"

    def test_constructor_transition_rolls_correct(
        self, authorized: ChromiumDriver
    ) -> None:
        authorized.find_element(By.XPATH, Locator.btn_fillings).click()
        WebDriverWait(authorized, self._TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locator.header_fillings)
            )
        )
        authorized.find_element(By.XPATH, Locator.btn_rolls).click()
        header = (
            WebDriverWait(authorized, self._TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_rolls)
                )
            )
            .text
        )
        authorized.quit()
        assert header == "Булки"

    def test_constructor_transition_sauces_correct(
        self, authorized: ChromiumDriver
    ) -> None:
        authorized.find_element(By.XPATH, Locator.btn_sauces).click()
        header = (
            WebDriverWait(authorized, self._TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_sauces)
                )
            )
            .text
        )
        authorized.quit()
        assert header == "Соусы"
