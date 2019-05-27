"""Conftest"""
import sys
import pytest
import urllib.parse
import platform
import allure
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver

from Lesson6.selenium.models.page_objects.login_page import LoginPage
from Lesson6.selenium.models.page_objects.products_page import ProductPage
from Lesson6.selenium.log.write_log import TestListener


server = Server(r"D:\browsermob\browsermob-proxy-2.1.4\bin\browsermob-proxy")
server.start()

proxy = server.create_proxy()
proxy.new_har()


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {"browser": request.config.getoption("--browser"),
         "address": request.config.getoption("--address"),
         "os_platform": environment_info[0],
         "system": environment_info[1]})
    yield


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    system = platform.system()
    return os_platform, system


def pytest_addoption(parser):
    """Adding options to command line"""
    parser.addoption("--address", action="store",
                     default="http://192.168.88.132/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--wait", action="store", default=10, help="Implicity wait")


@allure.title("Getting browser")
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
        driver.maximize_window()
        wd = EventFiringWebDriver(driver, TestListener())
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()


@pytest.fixture
@allure.title("Opening login page anf returning it")
def open_login_page(driver, request):
    """Opening admin login page"""
    url = 'opencart/admin/'
    driver.get("".join([request.config.getoption("--address"), url]))
    return LoginPage(driver)

#
# @pytest.fixture(params=[("admin", "admin")])
# def param_test(request):
#     return request.param[0], request[1]


@pytest.fixture
def login(open_login_page, user, password):
    """Logging in"""
    open_login_page.set_username(user)
    open_login_page.set_password(password)
    open_login_page.login()
    open_login_page.get_photo("login.png")


@pytest.fixture
def open_product_page(driver):
    """Opening product page"""
    driver.find_element_by_css_selector("[class=close]").click()
    driver.find_element_by_css_selector("#menu-catalog a").click()
    driver.find_element_by_link_text("Products").click()
    return ProductPage(driver)
