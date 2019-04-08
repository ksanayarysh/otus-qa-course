"""Проверки по показу пивоварен"""
import json
import requests
import pytest
import basic


@pytest.mark.brewery
def test_brewery():
    """
    Проверяем, что основная страница открывается и основные проверки проходят
    по умолчанию на странице должно быть 20 пивоварен
    """
    response = requests.get("https://api.openbrewerydb.org/breweries")
    basic.base_check(response)
    breweries = json.loads(response.text)
    assert len(breweries) == 20


PAGES = [i * 10 for i in range(1, 40)]
PER_PAGE_COUNT = [20, 50]


@pytest.mark.parametrize("page", PAGES)
@pytest.mark.parametrize("per_page", PER_PAGE_COUNT)
@pytest.mark.brewery
def test_pages(page, per_page):
    """
    Проверяем, сколько показывается пивоварен на странице, если параметр параметр per_page
    проверяем постраничный показ
    :param page: номер страницы
    :param per_page: количество пивоварен на странице
    """
    if page * per_page < 8000:
        response = requests.get(
            "https://api.openbrewerydb.org/breweries?page=" +
            str(page) + "&per_page=" + str(per_page))
        basic.base_check(response)
