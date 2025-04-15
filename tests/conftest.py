import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_options():
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.maximize_window()

    yield

    browser.quit()
