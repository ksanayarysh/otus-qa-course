"""Functions for working with login page"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Lesson6.selenium.models.page import BasePage
from Lesson6.selenium.models.locator import BaseLocators, LoginPageLocators


class LoginPage(BasePage):
    """Class for Login Page"""

    def set_username(self, username):
        """setting username"""
        try:
            user_name_field = self.driver.find_element(*LoginPageLocators.USERNAME)
            self._clear_element_(user_name_field)
            user_name_field.send_keys(username)
        except NoSuchElementException:
            print("No user name")

    def set_password(self, password):
        """setting password"""
        try:
            password_field = self.driver.find_element(*LoginPageLocators.PASSWORD)
            self._clear_element_(password_field)
            password_field.send_keys(password)
        except NoSuchElementException:
            print("No password")

    def login(self):
        """press "log in" button"""
        try:
            self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()
            WebDriverWait(self.driver, 10).until(EC.title_is, "Dashboard")
        except NoSuchElementException:
            print("Can't log in")
