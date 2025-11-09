import allure
import pytest
from selene import browser

@pytest.fixture(scope='function')
def setup_browser_realty():


    # Базовые настройки Selene
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://2gis.ru/ruza/realty/sale'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.type_by_js = False
    browser.config.hold_browser_open = False
    yield browser
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id: ' + session_id):
        browser.quit()

    with open("video.mp4", "rb") as video_file:
        allure.attach(
            video_file.read(),
            name="video",  # Название вложения в отчёте
            attachment_type=allure.attachment_type.MP4
        )

    browser.quit()

@pytest.fixture(scope='function')
def setup_browser_filter():


    # Базовые настройки Selene
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://2gis.ru/ruza/'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.type_by_js = False
    browser.config.hold_browser_open = False
    yield browser

    browser.quit()

@pytest.fixture(scope='function')
def setup_browser_form():


    # Базовые настройки Selene
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://2gis.ru'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.type_by_js = False
    browser.config.hold_browser_open = False
    yield browser

    browser.quit()