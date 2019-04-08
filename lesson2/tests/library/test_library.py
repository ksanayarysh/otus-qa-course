"""Тестирование API cdnjs.com"""
import json
import requests
import pytest

BASE_URL = "https://api.cdnjs.com/libraries"
HUMAN = ["&output=human"]
SEARCH = ["", "?search=ajax", "?search=jquery", "?search=ractive"]
FIELDS = ["fields=version", "fields=description", "fields=homepage,keywords",
          "fields=license,repository,autoupdate,author,assets"]
NAMES = ["jquery"]


@pytest.mark.parametrize("library,content_type", [("/jquery", "application/json"),
                                                  ("/jquery?output=human", "text/html")])
@pytest.mark.library
def test_name(library, content_type):
    """Тестируем конкретную библиотеку как json и human"""
    response = requests.get(BASE_URL + library)
    assert response.status_code == 200
    assert content_type in response.headers["Content-Type"]


@pytest.mark.parametrize("current_search", SEARCH)
@pytest.mark.parametrize("current_field", FIELDS)
@pytest.mark.library
def test_get_all(current_search, current_field):
    """Тестируем json все, поиск, доступ по названию с разными комбинациями полей"""
    url = BASE_URL + current_search
    if current_search != "":
        url += "&"
    else:
        url += "?"
    url += current_field
    response = requests.get(url)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    result = json.loads(response.text)
    assert len(result['results']) == result["total"]


@pytest.mark.parametrize("current_search", SEARCH)
@pytest.mark.parametrize("current_field", FIELDS)
@pytest.mark.parametrize("human", HUMAN)
@pytest.mark.library
def test_get_all_human(current_search, current_field, human):
    """
    Тестируем просмотр для человека все, поиск, доступ по названию с разными комбинациями полей
    """
    url = BASE_URL + current_search
    if current_search != "":
        url += "&"
    else:
        url += "?"
    url = url + current_field + human
    response = requests.get(url)
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]
