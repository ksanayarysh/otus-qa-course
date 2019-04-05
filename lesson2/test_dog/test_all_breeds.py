from datetime import datetime
import pytest
import requests

start_url = 'https://dog.ceo/api'
urls = "breeds/list/all", "breeds/image/random", "breeds/image/random/3"


@pytest.mark.parametrize("start", [start_url])
@pytest.mark.parametrize("url", urls)
def test_breed_list_all(url, start):
    """Заходим на основную страницу, проверяем, что дата сегодня, ответ 200, тип  ok,"""
    response = requests.get('/'.join([start, url]))
    assert datetime.now().strftime("%d %b %Y") in response.headers['Date']
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert isinstance(response.json(), dict)


