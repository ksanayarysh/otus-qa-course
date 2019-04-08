"""Получаем пивоварню по id"""
import json
import pytest
import requests
import basic


BREWERY_IDS = [i * 100 for i in range(1, 80)]


@pytest.mark.parametrize("brewery_id", BREWERY_IDS)
@pytest.mark.brewery
def test_get_brewery(brewery_id):
    """Пивоварня по id от 10 до 8000 через 100, базовые проверки"""
    response = requests.get("/".join(["https://api.openbrewerydb.org/breweries", str(brewery_id)]))
    basic.base_check(response)
    brewery = json.loads(response.text)
    assert isinstance(brewery, dict)
