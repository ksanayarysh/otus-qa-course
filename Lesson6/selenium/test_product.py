"""Тесты"""
import os

import pytest
import sqlite3


@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login")
@pytest.mark.parametrize("user,password", [("admin", "admin")])
@pytest.mark.usefixtures("open_login_page")
@pytest.mark.Product
class TestProductPage:
    """Tests for product page"""

    def test_mod_product(self, open_product_page):
        """Change product name from Some to Some new Stuff"""
        product_page = open_product_page
        new_name = "Some new stuff"
        old_names = product_page.get_product_names()
        product_page.modify_product("", new_name)
        assert product_page.successfully_modified() is True
        product_page.get_photo("mod_name.png")
        product_page.filter_product_by_name("")
        new_names = product_page.get_product_names()
        assert new_name in new_names
        assert len(old_names) == len(new_names)

    def test_delete_product(self, open_product_page):
        """Test for deleting first product """
        product_page = open_product_page
        count = product_page.get_all_quantity()
        product_page.delete_product("")
        product_page.get_photo("del_name.png")
        assert (count - 1) == product_page.get_all_quantity()

    def test_product_name_all_pages(self, open_product_page):
        """Shows list of product names"""
        print(open_product_page.get_product_names())

    @pytest.mark.right_adding
    def test_add_product(self, open_product_page):
        """Test for adding product"""
        product_page = open_product_page
        old_names = product_page.get_product_names()
        product_page.add_product()
        assert product_page.title() == "Products"
        product_page.get_photo("add_name.png")
        new_names = product_page.get_product_names()
        assert all([i in new_names for i in old_names])
        assert len(new_names) == len(old_names) + 1


def test():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    base_path = "/".join([dir_path, "log/logs/log2.db"])
    print(base_path)
    conn = sqlite3.connect(base_path)
    cursor = conn.cursor()
    result = cursor.execute("select * from  log ")
    for e in result:
        print(e)
