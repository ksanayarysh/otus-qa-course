"""Проверяем страницы список всех пород, слуачйное изображение, 3 случайных изображения """

from datetime import datetime
import pytest
import requests

START_URL = 'https://dog.ceo/api'
URLS = "breeds/list/all", "breeds/image/random", "breeds/image/random/3"


@pytest.mark.parametrize("start", [START_URL])
@pytest.mark.parametrize("url", URLS)
@pytest.mark.dogs
def test_breed_list_all(url, start):
    """Заходим на основную страницу, проверяем, что дата сегодня, ответ 200, тип  ok,"""
    response = requests.get('/'.join([start, url]))
    assert datetime.now().strftime("%d %b %Y") in response.headers['Date']
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert isinstance(response.json(), dict)
