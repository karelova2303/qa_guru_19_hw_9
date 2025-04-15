import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_options():
    browser.config.base_url = 'https://demoqa.com'
    # browser.driver.maximize_window()
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    browser.execute_script("document.body.style.zoom = '0.75'")

    yield

    browser.quit()
