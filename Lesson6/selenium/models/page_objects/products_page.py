"""
Product page
"""
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lesson6.selenium.models.locator import ProductPageLocators
from Lesson6.selenium.models.page import BasePage

PRODUCT_IMAGES_PATH = ("duck", "dog", "kitty")

class ProductPage(BasePage):
    """Working with Product Page """
    def add_product(self):
        """Adding product"""
        product_name = "".join(["some_product", str(time.time())])
        self.press_add_button()
        self.set_product_name(product_name)
        self.set_meta_tag_title("Title")
        self.press_data()
        self.set_model("Model")
        self.set_price(2000)
        self.set_quantity(1000)
        self.press_image()
        self.add_image()
        self.save()

    def press_add_button(self):
        """Press  + button"""
        try:
            self.driver.find_element(*ProductPageLocators.ADD).click()
        except NoSuchElementException:
            print("No add button")


    def set_product_name(self, product_name):
        """Setting product name"""
        try:
            self._clear_element_(self.driver.find_element(*ProductPageLocators.PRODUCT_NAME))
            self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(product_name)
        except NoSuchElementException:
            print("No name text field")

    def set_meta_tag_title(self, meta_tag_title):
        """Setting meta title"""
        try:
            self._clear_element_(self.driver.find_element(*ProductPageLocators.META_TAG_TITLE))
            self.driver.find_element(*ProductPageLocators.META_TAG_TITLE).send_keys(meta_tag_title)
        except NoSuchElementException:
            print("No meta tag")

    def set_model(self, model_name):
        """Setting model"""
        try:
            model = self.driver.find_element(*ProductPageLocators.MODEL_NAME)
            self._clear_element_(model)
            model.send_keys(model_name)
        except NoSuchElementException:
            print("No model name")

    def set_price(self, value):
        """Setting price"""
        try:
            price = self.driver.find_element(*ProductPageLocators.PRICE)
            self._clear_element_(price)
            price.send_keys(value)
        except NoSuchElementException:
            print("No price")

    def set_quantity(self, value):
        """Setting quantity"""
        try:
            quantity = self.driver.find_element(*ProductPageLocators.QUANTITY)
            self._clear_element_(quantity)
            quantity.send_keys(value)
        except NoSuchElementException:
            print("No quantity")

    def press_data(self):
        """Pressing data tab"""
        try:
            self.driver.find_element(*ProductPageLocators.DATA).click()
        except NoSuchElementException:
            print("No data tab")

    def press_image(self):
        """Pressing image tab"""
        try:
            self.driver.find_element(*ProductPageLocators.IMAGE).click()
        except NoSuchElementException:
            print("No data tab")

    def save(self):
        """Нажать кнопку сохранить"""
        try:
            self.driver.find_element(*ProductPageLocators.SAVE).click()
        except NoSuchElementException:
            print("No save button")

    def filter_product_by_name(self, name):
        """Filter product by name"""
        filter_field = self.driver.find_element(*ProductPageLocators.FILTER_NAME)
        self._clear_element_(filter_field)
        filter_field.send_keys(name)
        self.driver.find_element(*ProductPageLocators.FILTER_BUTTON).click()

    def if_is_any_product(self):
        """Getting product quantity, current page """
        return len(self.driver.find_elements(*ProductPageLocators.PRODUCT_TABLE))

    def get_all_quantity(self):
        return len(self.get_product_names())

    def get_products(self):
        """Getting product web elements current page"""
        return self.driver.find_elements(*ProductPageLocators.PRODUCT_TABLE)

    def get_product_names(self):
        """Getting elements names"""
        names = []
        while True:
            if self.if_is_any_product() > 0:
                products = self.get_products()
                if products:
                    for product in products:
                        names.append(product.find_elements(*ProductPageLocators.TD)[2].text)
                else:
                    break

                if self.check_pagination():
                    is_next_button = self.click_next_button()
                    if not is_next_button:
                        break
                else:
                    break

        return names

    def delete_product(self, name):
        """Deleting product"""
        self.filter_product_by_name(name)
        quantity = self.if_is_any_product()
        if quantity:
            try:
                products = self.get_products()
                products[0].find_element(*ProductPageLocators.CHECK_BOX).click()
                self.driver.find_element(*ProductPageLocators.DELETE).click()
                alert = self.driver.switch_to.alert
                alert.accept()
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(ProductPageLocators.SUCCESS))
                self.filter_product_by_name("")
            except(NoSuchElementException, TimeoutException):
                print("Can't delete")

    def modify_product(self, old_name, new_name):
        """Modifying product, changing its name from old_name to new_name"""
        self.filter_product_by_name(old_name)
        if self.if_is_any_product():
            products = self.get_products()
            products[0].find_element(*ProductPageLocators.MODIFY).click()

            self.set_product_name(new_name)
            self.save()

    def check_pagination(self):
        """Check if there is more than one pages of products"""
        pagination = self.driver.find_elements(*ProductPageLocators.PAGINATION)
        return len(pagination) > 0

    def click_next_button(self):
        """Click > button"""
        next_page = self._wait_element_(*ProductPageLocators.NEXT_PAGE, delay=5)
        if next_page:
            next_page.click()
        return next_page is not None

    def add_image(self):
        """Adding three images"""
        image = self.driver.find_element(*ProductPageLocators.PRIMARY_IMAGE)
        self.unhide_input(image)
        image.send_keys("".join(["catalog/", PRODUCT_IMAGES_PATH[0], ".jpg"]))
        self.press_add_image()

        image = self.driver.find_element(*ProductPageLocators.IMAGE1)
        self.unhide_input(image)
        image.send_keys("".join(["catalog/", PRODUCT_IMAGES_PATH[1], ".jpg"]))
        self.press_add_image()

        image = self.driver.find_element(*ProductPageLocators.IMAGE2)
        self.unhide_input(image)
        image.send_keys("".join(["catalog/", PRODUCT_IMAGES_PATH[2], ".jpg"]))

    def unhide_input(self, element):
        """Making input to be visible"""
        self.driver.execute_script("arguments[0].removeAttribute('type')", element)

    def press_add_image(self):
        """Pressing add image button"""
        self.driver.find_element(*ProductPageLocators.ADD_IMAGE).click()

    def successfully_modified(self):
        return len(self.driver.find_elements(*ProductPageLocators.SUCCESS)) > 0
