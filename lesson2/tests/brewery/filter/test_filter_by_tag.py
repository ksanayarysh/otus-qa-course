"""Проверяем фильтр по тегу"""
import json
import requests
import pytest
import basic

TAGS = ["dog-friendly", "patio", "food-service", "food-truck", "tours"]


@pytest.mark.parametrize("tag", TAGS)
@pytest.mark.brewery
def test_filter_by_tag_case(tag):
    """Проверяем, что результаты не зависят от регистра + базовые проверки"""
    basic.check_case("https://api.openbrewerydb.org/breweries?by_tag=", tag, "")


@pytest.mark.parametrize("tag", TAGS)
@pytest.mark.brewery
def test_filter_by_tag_is_same(tag):
    """
    Проверяем, что tag действительно существует для данной пивоварни
    """
    response = requests.get("https://api.openbrewerydb.org/breweries?by_tag=" + tag)
    breweries = json.loads(response.text)
    for brewery in breweries:
        assert tag in brewery['tag_list']
