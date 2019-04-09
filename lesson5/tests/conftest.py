"""Conftest"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions

def get_chrome():
    """Создать chrome"""
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)

def get_firefox():
    """Создать firefox"""
    options = FirefoxOptions()
    options.headless = True
    options.set_preference("maximized", True)
    return webdriver.Firefox(options=options)

def get_ie():
    """Создать Ie"""
    options = IeOptions()
    options.headless = True
    options.add_argument("--start-maximized")
    return webdriver.Ie(options=options)

@pytest.fixture
def driver(request, get_browser):
    """Выбираем браузер в зависимости от параметров командной строки"""
    if get_browser == "chrome":
        web_driver = get_chrome()
    else:
        if get_browser == "firefox":
            web_driver = get_firefox()
        else:
            web_driver = get_ie()

    web_driver.implicitly_wait(20)

    request.addfinalizer(web_driver.quit)
    return web_driver


def pytest_addoption(parser):
    """Добавляем опции командной строки"""
    parser.addoption("--b", action="store")
    parser.addoption("--address", action="store")


@pytest.fixture(autouse=True)
def get_browser(request):
    """Получаем имя браузера в зависимости из option"""
    return request.config.getoption("--b")


@pytest.fixture(autouse=True)
def get_url(request):
    """Получаем базовый url"""
    return request.config.getoption("--address")
