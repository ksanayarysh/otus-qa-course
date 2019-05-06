"""Тесты"""
import pytest
import time


@pytest.mark.usefixtures("product_page")
@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login")
@pytest.mark.parametrize("user", ["admin"])
@pytest.mark.parametrize("password", ["admin"])
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestProductPage:
    """Tests for product page"""

    def test_add_product(self, product_page):
        """Test for adding product"""
        old_names = product_page.get_product_names()
        product_page.add_product()
        new_names = product_page.get_product_names()
        assert all([i in new_names for i in old_names])
        assert len(new_names) == len(old_names) + 1

    def test_mod_product(self, product_page):
        """Change product name from Some to Some new Stuff"""
        new_name = "Some new stuff"
        old_names = product_page.get_product_names()
        product_page.modify_product("i", new_name)
        new_names = product_page.get_product_names()
        assert new_name in new_names
        assert len(old_names) == len(new_names)

    def test_delete_product(self, product_page):
        """Test for deleting product first of those that contains s letter"""
        count = product_page.get_product_quantity()
        product_page.delete_product("s")
        assert (count - 1) == product_page.get_product_quantity()

    def test_product_name_all_pages(self, product_page):
        """Shows list of product names"""
        print(product_page.get_product_names())


