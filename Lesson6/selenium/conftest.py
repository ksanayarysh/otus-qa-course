"""Conftest"""
import sys
import pytest
import urllib.parse
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver

from Lesson6.selenium.models.page_objects.login_page import LoginPage
from Lesson6.selenium.models.page_objects.products_page import ProductPage
from Lesson6.selenium.models.page_objects.download_page import DownloadPage
from Lesson6.selenium.log.write_log import TestListener

server = Server(r"C:\Python\browsermob-proxy-2.1.4\bin\browsermob-proxy")
server.start()

proxy = server.create_proxy()
proxy.new_har()


def pytest_addoption(parser):
    """Adding options to command line"""
    parser.addoption("--address", action="store",
                     default="http://192.168.145.130/", help="Opencart web address")
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
        wd = EventFiringWebDriver(webdriver.Firefox(firefox_profile=profile, capabilities=capabilities), TestListener())
        wd.maximize_window()
    elif browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        url = urllib.parse.urlparse(proxy.proxy).path
        chrome_options.add_argument('--proxy-server=%s' % url)
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['loggingPrefs'] = {'performance': 'ALL'}
        driver = webdriver.Chrome(desired_capabilities=capabilities, options=chrome_options)
        driver.implicitly_wait(wait)
        wd = EventFiringWebDriver(driver, TestListener())
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()


@pytest.fixture
def open_login_page(driver, request):
    """Opening admin login page"""
    url = 'opencart/admin/'
    driver.get("".join([request.config.getoption("--address"), url]))
    return LoginPage(driver)


@pytest.fixture(params=[("admin", "admin")])
def param_test(request):
    return request.param

@pytest.fixture
def login(open_login_page, param_test):
    """Logging in"""
    (user, password) = param_test
    open_login_page.set_username(user)
    open_login_page.set_password(password)
    open_login_page.login()


@pytest.fixture
def open_download_page(driver):
    """Opening download page"""
    #driver.get("http://192.168.88.132/opencart/admin/index.php?route=catalog/download/add")
    driver.find_element_by_css_selector("[class=close]").click()
    driver.find_element_by_css_selector("#menu-catalog a").click()
    driver.find_element_by_link_text("Downloads").click()
    return DownloadPage(driver)


@pytest.fixture
def open_product_page(driver):
    """Opening product page"""
    driver.find_element_by_css_selector("[class=close]").click()
    driver.find_element_by_css_selector("#menu-catalog a").click()
    driver.find_element_by_link_text("Products").click()
    return ProductPage(driver)
