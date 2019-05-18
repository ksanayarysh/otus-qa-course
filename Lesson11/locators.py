"""Locators"""
from selenium.webdriver.common.by import By


class CustomMenuLocators:
    USER_NAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class=\"btn btn-primary\"]")
    MENUS = (By.CSS_SELECTOR, "#custommenu-management li dl dt")
    SOURCE = (By.XPATH, "//li[@id='custommenu-child-item-41']/dl/dt")
    TARGET = (By.XPATH, "//li[@id='custommenu-item-3']/dl/dt")
