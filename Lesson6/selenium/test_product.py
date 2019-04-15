"""Тесты"""
import pytest


@pytest.mark.usefixtures("product_page")
@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login")
@pytest.mark.parametrize("user", ["admin"])
@pytest.mark.parametrize("password", ["admin"])
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestProductPage:

    def test_add_product(self, product_page):
        """Проверяем добавление продукта
        получаем старые названия
        добавляем
        получаем новые
        проверяем, что новое там есть и старые не потерялись"""
        old_names = product_page.get_product_names()
        product_page.add_product()
        new_names = product_page.get_product_names()
        assert all([i in new_names for i in old_names])
        assert len(new_names) == len(old_names) + 1

    def test_mod_product(self, product_page):
        """Проверяем изменение названия продукта"""
        new_name = "Some new stuff"
        old_names = product_page.get_product_names()
        product_page.modify_product("Some", new_name)
        new_names = product_page.get_product_names()
        assert new_name in new_names
        assert len(old_names) == len(new_names)

    def test_delete_product(self, product_page):
        """Проверяем удаление продукта"""
        count = product_page.get_product_quantity()
        if product_page.delete_product("Some"):
            assert (count - 1) == product_page.get_product_quantity()
