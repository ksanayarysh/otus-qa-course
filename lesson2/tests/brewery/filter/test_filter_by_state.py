"""
Проверяем фильтр по штату и сортировку
Еще проверить, правильно ли сортируется
"""

import json
import pytest
import requests
import basic

STATES = ["new_york", "alabama", "alaska", "arizona"]
SORT_ORDER = ["", "&sort=type,-name"]


@pytest.mark.parametrize("state", STATES)
@pytest.mark.parametrize("sort", SORT_ORDER)
@pytest.mark.brewery
def test_filter_by_state_case(state, sort):
    """Проверяем, что результаты не зависят от регистра + базовые проверки"""
    basic.check_case("https://api.openbrewerydb.org/breweries?by_state=", state, sort)


@pytest.mark.parametrize("state", STATES)
@pytest.mark.brewery
def test_filter_by_state_is_same(state):
    """
    Проверяем, что название то же самое,что передан в запросе
    в том числе поиск по части названия
    """
    response = requests.get("https://api.openbrewerydb.org/breweries?by_state=" + state)
    breweries = json.loads(response.text)
    for brewery in breweries:
        assert state.lower().replace("_", " ") in brewery['state'].lower()
