"""Testing moving custom menu"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from Lesson11.locators import CustomMenuLocators
from Lesson11.test_data import CUSTOM_MENU_URL, USER_NAME, PASSWORD


@pytest.fixture(scope="session")
def chrome_browser():
    """Driver"""
    wd = webdriver.Chrome()
    yield wd
    wd.quit()


@pytest.fixture
def login(chrome_browser):
    """Logging in"""
    chrome_browser.get(CUSTOM_MENU_URL)
    chrome_browser.find_element(*CustomMenuLocators.USER_NAME).send_keys(USER_NAME)
    chrome_browser.find_element(*CustomMenuLocators.PASSWORD).send_keys(PASSWORD)
    chrome_browser.find_element(*CustomMenuLocators.LOGIN_BUTTON).click()


def test_move_custom_menu(chrome_browser, login):
    """Moving the source menu into the target"""
    old_len = len(chrome_browser.find_elements(*CustomMenuLocators.MENUS))

    source = chrome_browser.find_element(*CustomMenuLocators.SOURCE)
    target = chrome_browser.find_element(*CustomMenuLocators.TARGET)
    ActionChains(chrome_browser).drag_and_drop(source, target).perform()
    new_len = len(chrome_browser.find_elements(*CustomMenuLocators.MENUS))
    assert old_len == new_len
