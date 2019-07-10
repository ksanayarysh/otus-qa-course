
"""Conftest"""
import sys
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver

from Lesson6.selenium.log.log_to_db_listener import TestListenerDb
from Lesson6.selenium.models.page_objects.login_page import LoginPage
from Lesson6.selenium.models.page_objects.products_page import ProductPage


def pytest_addoption(parser):
    """Adding options to command line"""
    parser.addoption("--address", action="store",
                     default="http://localhost/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--wait", action="store", default=10, help="Implicity wait")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Getting driver according to command line option"""
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': wait, 'pageLoad': 30000, 'script': 1000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = EventFiringWebDriver(webdriver.Firefox(firefox_profile=profile,
                                                    capabilities=capabilities), TestListenerDb())
        wd.maximize_window()
    elif browser == 'chrome':
        chrome_options = Options()

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path="/usr/local/bin/chromedriver")

        driver.implicitly_wait(wait)
        driver.maximize_window()
        wd = EventFiringWebDriver(driver, TestListenerDb())
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()


@pytest.fixture
def open_login_page(driver, request):
    """Opening admin login page"""
    url = 'opencart/admin/'
    address = "/".join(["http:/", request.config.getoption("--address"), url])
    driver.get(address)
    return LoginPage(driver)


@pytest.fixture
def login(open_login_page, user, password):
    """Logging in"""
    open_login_page.set_username(user)
    open_login_page.set_password(password)
    open_login_page.login()
    # open_login_page.get_photo("login.png")


@pytest.fixture
def open_product_page(driver):
    """Opening product page"""
    driver.find_element_by_css_selector("[class=close]").click()
    driver.find_element_by_css_selector("#menu-catalog a").click()
    driver.find_element_by_link_text("Products").click()
    return ProductPage(driver)
