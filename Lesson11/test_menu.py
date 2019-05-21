"""Testing moving custom menu"""

from selenium.webdriver.common.action_chains import ActionChains

from Lesson11.locators import CustomMenuLocators


def test_move_custom_menu(driver, login):
    """Moving the source menu into the target"""
    old_len = len(driver.find_elements(*CustomMenuLocators.MENUS))

    source = driver.find_element(*CustomMenuLocators.SOURCE)
    target = driver.find_element(*CustomMenuLocators.TARGET)
    ActionChains(driver).drag_and_drop(source, target).perform()
    new_len = len(driver.find_elements(*CustomMenuLocators.MENUS))
    assert old_len == new_len
