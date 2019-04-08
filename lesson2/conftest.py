"""Conftest"""
import pytest

def pytest_addoption(parser):
    """Опция командной строки"""
    parser.addoption("--site", action="store", default="None")


def pytest_collection_modifyitems(config, items):
    """Получаем и в зависимости от ее значения скипим тесты"""
    value = config.getoption("--site")
    skip = pytest.mark.skip(reason="no need to run")
    for item in items:
        if value not in item.keywords:
            item.add_marker(skip)
