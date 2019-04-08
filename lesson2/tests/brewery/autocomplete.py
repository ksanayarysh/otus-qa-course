"""Проверка autocomplete и search"""
import json
import requests
import pytest
import basic


QUERIES = ["dog", "cat", "mouse"]


@pytest.mark.parametrize("query", QUERIES)
@pytest.mark.brewery
def test_autocomplete(query):
    """Проверка autocomplete"""
    response = requests.get("/".join(["https://api.openbrewerydb.org/breweries/autocomplete?query=",
                                      query]))
    basic.base_check(response)
    brewery = json.loads(response.text)
    print(brewery)


@pytest.mark.parametrize("query", QUERIES)
@pytest.mark.brewery
def test_search(query):
    """Проверка search"""
    response = requests.get("/".join(["https://api.openbrewerydb.org/breweries/search?query=",
                                      query]))
    basic.base_check(response)
    brewery = json.loads(response.text)
    print(brewery)
