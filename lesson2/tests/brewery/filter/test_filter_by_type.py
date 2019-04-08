"""Проверка сортивроки по типам"""
import json
import requests
import pytest
import basic

TYPES = ["micro", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor"]


@pytest.mark.parametrize("type_of_brewery", TYPES)
@pytest.mark.brewery
def test_filter_by_type_case(type_of_brewery):
    """Проверяем, что результаты не зависят от регистра + базовые проверки"""
    basic.check_case("https://api.openbrewerydb.org/breweries?by_type=", type_of_brewery, "")


@pytest.mark.parametrize("type_of_brewery", TYPES)
@pytest.mark.brewery
def test_filter_by_type_is_same(type_of_brewery):
    """
    Проверяем, что название то же самое,что передан в запросе
    в том числе поиск по части названия
    """
    response = requests.get("https://api.openbrewerydb.org/breweries?by_type=" + type_of_brewery)
    breweries = json.loads(response.text)
    for brewery in breweries:
        assert type_of_brewery.lower() == brewery['brewery_type'].lower()
