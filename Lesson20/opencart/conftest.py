"""Conftest"""
import sys
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Adding options to command line"""
    parser.addoption("--address", action="store",
                     default="http://192.168.88.132/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--wait", action="store", default=10, help="Implicity wait")


@pytest.fixture(scope="session")
def wd(request):
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
        wd = webdriver.Firefox(firefox_profile=profile, capabilities=capabilities,
                                                    executable_path=r'/home/lu/Downloads/geckodriver')
        wd.maximize_window()
    elif browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['loggingPrefs'] = {'performance': 'ALL'}
        driver = webdriver.Chrome(desired_capabilities=capabilities, options=chrome_options)
        driver.implicitly_wait(wait)
        driver.maximize_window()
        wd = driver
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()
