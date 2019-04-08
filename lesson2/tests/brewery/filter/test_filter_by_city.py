"""Проверка фильтра по городу"""
import json
import requests
import pytest
import basic

CITIES = ["Birmingham", "Anchorage", "Lake Havasu City", "Surprise", "Tucson", "New"]


@pytest.mark.parametrize("city", CITIES)
@pytest.mark.brewery
def test_filter_by_city_case(city):
    """
    Проверяем, что при фильтре по городу все ok и поиск в
    нижнем регистре дает те же результаты, что и в верхнем
    :param city: город
    """
    basic.check_case("https://api.openbrewerydb.org/breweries?by_city=", city, "")


@pytest.mark.parametrize("city", CITIES)
@pytest.mark.brewery
def test_filter_by_city_is_same(city):
    """
    Проверяем, что город тот же самый,что передан в запросе
    в том числе поиск по части названия
    :param city: город
    """
    response = requests.get("https://api.openbrewerydb.org/breweries?by_city=" + city)
    breweries = json.loads(response.text)
    for brewery in breweries:
        assert city.lower() in brewery['city'].lower()
