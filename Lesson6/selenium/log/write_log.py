"""Logging"""
import logging
import datetime as dt

from selenium.webdriver.support.events import AbstractEventListener

logging.basicConfig(filename="log/sample.log", level=logging.INFO)


def msg_with_date(msg):
    """Adding date"""
    return ":".join([str(dt.datetime.now()), msg])


class TestListener(AbstractEventListener):
    """Class for writing logs and taking screenshots"""
    def before_navigate_to(self, url, driver):
        logging.info(msg_with_date("".join(["Before navigate to ", url])))

    def after_navigate_to(self, url, driver):
        logging.info(msg_with_date("".join(["After navigate to ", url])))

    def on_exception(self, exception, driver):
        logging.error(exception)
        now = dt.datetime.now()
        filename = "".join(["screenshots/exception", now.strftime("%d-%m-%Y-%H-%M"), ".png"])
        print(filename)
        driver.get_screenshot_as_file(filename)
