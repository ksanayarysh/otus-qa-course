import pytest
from selenium import webdriver

HUB = "http://192.168.0.102:4444/wd/hub"


@pytest.fixture
def chrome_browser():
    wd = webdriver.Remote(HUB, desired_capabilities={"browserName": "chrome"})
    yield wd
    wd.quit()


@pytest.fixture
def firefox_browser():
    wd = webdriver.Remote(HUB, desired_capabilities={"browserName": "firefox"})
    yield wd
    wd.quit()

