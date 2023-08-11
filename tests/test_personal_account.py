from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locator


class TestPersonalAccount:
    _TIMEOUT: float = 2

    def test_personal_account_transition_successful(
        self, authorized: ChromiumDriver
    ) -> None:
        authorized.find_element(By.XPATH, Locator.btn_personal_account).click()
        button_text = (
            WebDriverWait(authorized, self._TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.btn_exit)
                )
            )
            .text
        )
        authorized.quit()
        assert button_text == "Выход"

    def test_personal_account_logout_user_logged_out(
        self, authorized: ChromiumDriver
    ) -> None:
        authorized.find_element(By.XPATH, Locator.btn_personal_account).click()
        WebDriverWait(authorized, self._TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locator.btn_exit)
            )
        ).click()
        header = (
            WebDriverWait(authorized, self._TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_authorization)
                )
            )
            .text
        )
        authorized.quit()
        assert header == "Вход"

    def test_personal_account_transition_constructor_through_button_successful(
        self, authorized: ChromiumDriver
    ) -> None:
        authorized.find_element(By.XPATH, Locator.btn_personal_account).click()
        authorized.find_element(By.XPATH, Locator.btn_constructor).click()
        header = (
            WebDriverWait(authorized, self._TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_main)
                )
            )
            .text
        )
        authorized.quit()
        assert header == "Соберите бургер"

    def test_personal_account_transition_constructor_through_logo_successful(
        self, authorized: ChromiumDriver
    ) -> None:
        authorized.find_element(By.XPATH, Locator.btn_personal_account).click()
        authorized.find_element(By.XPATH, Locator.logo).click()
        header = (
            WebDriverWait(authorized, self._TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, Locator.header_main)
                )
            )
            .text
        )
        authorized.quit()
        assert header == "Соберите бургер"
