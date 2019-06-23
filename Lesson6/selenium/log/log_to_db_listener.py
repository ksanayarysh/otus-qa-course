"""Logging to db"""
import datetime as dt
import os
import sqlite3

from selenium.webdriver.support.events import AbstractEventListener


def msg_with_date(msg):
    """Adding date"""
    return ":".join([str(dt.datetime.now()), msg])


class TestListenerDb(AbstractEventListener):
    def __init__(self):
        db_path = "/".join([os.path.dirname(os.path.abspath(__file__)), "logs/log2.db"])
        print(db_path)
        self.conn = sqlite3.connect(db_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def write(self, log, level="INFO"):
        self.conn.execute("INSERT INTO log VALUES(\"{0}\", \"{1}\")".format(log, level))
        self.conn.commit()

    """Class for writing logs and taking screenshots"""
    def before_navigate_to(self, url, driver):
        self.write(msg_with_date("".join(["Before navigate to ", url])))

    def after_navigate_to(self, url, driver):
        self.write(msg_with_date("".join(["After navigate to ", url])))
        # performance_log = driver.get_log("performance")
        # time_to_load = performance_log[-1].get('timestamp') - performance_log[0].get("timestamp")
        # self.write(" ".join(["Page load", url, str(time_to_load), 'ms']))

    def on_exception(self, exception, driver):
        self.write(exception)


