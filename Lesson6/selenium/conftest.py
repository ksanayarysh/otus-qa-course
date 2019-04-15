import time

import pytest
import sys

from selenium import webdriver

from Lesson6.selenium.models.page_objects.login_page import LoginPage
from Lesson6.selenium.models.page_objects.products_page import ProductPage


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.145.130/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = webdriver.Firefox(firefox_profile=profile, capabilities=capabilities)
        wd.maximize_window()
    elif browser == 'chrome':
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        wd = webdriver.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()

@pytest.fixture(scope="function")
def open_login_page(driver, request):
    print("open_login_page")
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="module")
def login_page(driver):
    """Получаем login page"""
    print("login_page")
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login(login_page, user, password):
    """заходим в админку"""
    print("login")
    login_page.set_username(user)
    login_page.set_password(password)
    login_page.login()
    time.sleep(10)


@pytest.fixture(scope="function")
def product_page(driver):
    print("product_page")
    return ProductPage(driver)

@pytest.fixture
def open_product_page(driver):
    print("open_product_page")
    driver.find_element_by_css_selector("[class=close]").click()
    driver.find_element_by_css_selector("#menu-catalog a").click()
    driver.find_element_by_link_text("Products").click()


