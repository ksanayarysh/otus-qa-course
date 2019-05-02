"""Conftest"""
import sys
import pytest

from selenium import webdriver

from Lesson6.selenium.models.page_objects.login_page import LoginPage
from Lesson6.selenium.models.page_objects.products_page import ProductPage


def pytest_addoption(parser):
    """Adding options to command line"""
    parser.addoption("--address", action="store",
                     default="http://192.168.145.130/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--wait", action="store", default=10, help="Implicity wait")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Getting driver according to command line option"""
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': wait, 'pageLoad': 10000, 'script': 1000}
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
    """Opening admin login page"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="module")
def login_page(driver):
    """Getting login page object"""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login(login_page, user, password):
    """Logging in"""
    login_page.set_username(user)
    login_page.set_password(password)
    login_page.login()


@pytest.fixture(scope="function")
def product_page(driver):
    """Getting product page object"""
    return ProductPage(driver)


@pytest.fixture
def open_product_page(driver):
    """Opening product page"""
    driver.find_element_by_css_selector("[class=close]").click()
    driver.find_element_by_css_selector("#menu-catalog a").click()
    driver.find_element_by_link_text("Products").click()

