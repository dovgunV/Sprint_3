from typing import Iterator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium.webdriver import ChromiumDriver

from urls import BASE


@pytest.fixture
def driver() -> Iterator[ChromiumDriver]:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options)
    browser.get(BASE)
    yield browser
    browser.quit()
