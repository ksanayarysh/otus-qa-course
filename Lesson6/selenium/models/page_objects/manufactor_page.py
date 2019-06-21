from Lesson6.selenium.models.locator import ManufacturerLocators
from Lesson6.selenium.models.page import BasePage


class ManufacturerPage(BasePage):
    def __init__(self, wd):
        BasePage.__init__(self, wd)
        wd.find_element_by_css_selector("[class=close]").click()
        wd.find_element_by_css_selector("#menu-catalog a").click()
        wd.find_element_by_link_text("Manufacturers").click()

    def check_is_manufacturer_exists(self, name):
        mans = self.driver.find_elements(*ManufacturerLocators.MANUFACTURER_TABLE)
        for man in mans:
            man_name = man.find_elements_by_css_selector("td")
            if man_name[1].text == name:
                return True
        return False
