import pytest
from selenium import webdriver
import sys
from Lesson11.locators import CustomMenuLocators
from Lesson11.test_data import CUSTOM_MENU_URL, USER_NAME, PASSWORD

def pytest_addoption(parser):
    """Adding options to command line"""
    parser.addoption("--browser", action="store", default="cloud", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Getting driver according to command line option"""
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['loggingPrefs'] = {'performance': 'ALL'}
        wd = webdriver.Chrome(desired_capabilities=capabilities, options=chrome_options)
        wd.implicitly_wait(5)
        wd.maximize_window()
    elif browser == 'cloud':
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '52.0',
            'os': 'OS X',
            'os_version': 'Mojave',
            'resolution': '1920x1080',
            'name': 'Bstack-[Python] Sample Test'
        }
        wd = webdriver.Remote(command_executor='http://ksanaya1:64bR9TnV8YBFrZ1eu4qu@hub.browserstack.com:80/wd/hub',
                              desired_capabilities=desired_cap)

    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()


@pytest.fixture
def login(driver):
    """Logging in"""
    driver.get(CUSTOM_MENU_URL)
    driver.find_element(*CustomMenuLocators.USER_NAME).send_keys(USER_NAME)
    driver.find_element(*CustomMenuLocators.PASSWORD).send_keys(PASSWORD)
    driver.find_element(*CustomMenuLocators.LOGIN_BUTTON).click()


