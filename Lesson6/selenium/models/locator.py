"""Locators"""
from selenium.webdriver.common.by import By


class BaseLocators:
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")


class LoginPageLocators:
    """Locators for Login Page"""
    USERNAME = (By.ID, "input-username")
    USERNAME2 = (By.NAME, "username")
    USERNAME3 = (By.CSS_SELECTOR, "#input-username")
    USERNAME4 = (By.XPATH, "//*[@placeholder='Username']")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")


class ProductPageLocators:
    """Locators for Product Page"""
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    MODEL_NAME = (By.ID, "input-model")
    PRICE = (By.ID, "input-price")
    DATA = (By.CSS_SELECTOR, "[href=\"#tab-data\"]")
    SAVE = (By.CSS_SELECTOR, "[type=submit]")
    ADD = (By.CSS_SELECTOR, "[class=\"fa fa-plus\"]")
    MODIFY = (By.CSS_SELECTOR, "[class=\"fa fa-pencil\"]")
    DELETE = (By.CSS_SELECTOR, "[class=\"fa fa-trash-o\"]")
    QUANTITY = (By.CSS_SELECTOR, "[name=quantity]")
    FILTER_NAME = (By.CSS_SELECTOR, "[name=filter_name]")
    FILTER_BUTTON = (By.ID, "button-filter")
    PRODUCT_TABLE = (By.CSS_SELECTOR, "[class=\"table-responsive\"] tbody tr")
    CHECK_BOX = (By.CSS_SELECTOR, "[type=checkbox]")
    TD = (By.CSS_SELECTOR, "td")
    PAGINATION = (By.CSS_SELECTOR, "ul.pagination")
    NEXT_PAGE = (By.LINK_TEXT, ">")
    SUCCESS = (By.CLASS_NAME, "div.alert.alert-success.alert-dismissible")
