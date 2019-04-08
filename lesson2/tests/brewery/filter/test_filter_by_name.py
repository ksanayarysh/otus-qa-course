"""Проверка фильтра по названию пивоварни"""
import json
import requests
import pytest
import basic

NAMES = ["cooper", "Avondale", "Band", "Mudshark", "Brick"]


@pytest.mark.parametrize("name", NAMES)
@pytest.mark.brewery
def test_filter_by_name_case(name):
    """Проверяем, что результаты не зависят от регистра + базовые проверки"""
    basic.check_case("https://api.openbrewerydb.org/breweries?by_name=", name, "")


@pytest.mark.parametrize("name", NAMES)
@pytest.mark.brewery
def test_filter_by_name_is_same(name):
    """
    Проверяем, что название то же самое,что передан в запросе
    в том числе поиск по части названия
    """
    response = requests.get("https://api.openbrewerydb.org/breweries?by_name=" + name)
    breweries = json.loads(response.text)
    for brewery in breweries:
        assert name.lower() in brewery['name'].lower()
