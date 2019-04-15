"""
Product page
"""
from selenium.webdriver.common.keys import Keys
from Lesson6.selenium.models.locator import ProductPageLocators
from Lesson6.selenium.models.page import BasePage


class ProductPage(BasePage):
    """Добавить продукт"""
    def add_product(self):
        print("i'm add_product")
        self.press_add_button()
        self.set_product_name("Some product")
        self.set_meta_tag_title("Title")
        self.press_data()
        self.set_model("Model")
        self.set_price(2000)
        self.set_quantity(1000)
        self.save()

    def press_add_button(self):
        """Нажать кнопку +"""
        self.driver.find_element(*ProductPageLocators.ADD).click()

    def set_product_name(self, product_name):
        """Задать имя продукта"""
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(product_name)

    def set_meta_tag_title(self, meta_tag_title):
        """Meta title"""
        self.driver.find_element(*ProductPageLocators.META_TAG_TITLE).send_keys(meta_tag_title)

    def set_model(self, model):
        """Model"""
        self.driver.find_element(*ProductPageLocators.MODEL_NAME).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*ProductPageLocators.MODEL_NAME).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*ProductPageLocators.MODEL_NAME).send_keys(model)

    def set_price(self, price):
        """Цена"""
        self.driver.find_element(*ProductPageLocators.PRICE).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*ProductPageLocators.PRICE).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*ProductPageLocators.PRICE).send_keys(price)

    def set_quantity(self, quantity):
        """Количество"""
        self.driver.find_element(*ProductPageLocators.QUANTITY).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*ProductPageLocators.QUANTITY).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*ProductPageLocators.QUANTITY).send_keys(quantity)


    def press_data(self):
        """Нажать вкладку data"""
        self.driver.find_element(*ProductPageLocators.DATA).click()

    def save(self):
        """Нажать кнопку сохранить"""
        self.driver.find_element(*ProductPageLocators.SAVE).click()

    def find_product_by_name(self, name):
        """Поиск продукта"""
        self.driver.find_element(*ProductPageLocators.FILTER_NAME).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*ProductPageLocators.FILTER_NAME).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*ProductPageLocators.FILTER_NAME).send_keys(name)
        self.driver.find_element(*ProductPageLocators.FILTER_BUTTON).click()

    def get_product_quantity(self):
        """Ищем таблицу продуктов и проверяем что в ней есть элементы"""
        return len(self.driver.find_elements(*ProductPageLocators.PRODUCT_TABLE))

    def get_products(self):
        """Получить список продуктов в таблице"""
        return self.driver.find_elements(*ProductPageLocators.PRODUCT_TABLE)


    def get_product_names(self):
        """Получаeм названия продуктов"""
        if self.get_product_quantity() > 0:
            products = self.get_products()
            names = []
            if len(products) > 0:
                for product in products:
                    names.append(product.find_elements(*ProductPageLocators.TD)[2].text)
            return names

    def delete_product(self, name):
        """Удалить продукт"""
        self.find_product_by_name(name)
        if self.get_product_quantity():
            products = self.get_products()
            products[0].find_element(*ProductPageLocators.CHECK_BOX).click()
            self.driver.find_element(*ProductPageLocators.DELETE).click()
            alert = self.driver.switch_to_alert()
            alert.accept()
        else:
            return None
        self.find_product_by_name("")

    def modify_product(self, old_name, new_name):
        """Изменить продукт"""
        self.find_product_by_name(old_name)
        if self.get_product_quantity():
            products = self.get_products()
            products[0].find_element(*ProductPageLocators.MODIFY).click()
            self.set_product_name(new_name)
            self.save()
        self.find_product_by_name("")
