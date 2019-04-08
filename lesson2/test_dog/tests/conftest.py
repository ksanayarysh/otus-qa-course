import json
import pytest
import requests

base_url = 'https://dog.ceo/api'
base_breed_url = 'https://dog.ceo/api/breeds/list/all'


class APIClient:
    """Создаем API client"""
    def __init__(self, address=base_url):
        self.address = address

    def do_get(self, endpoint):
        url = "/".join([self.address, endpoint])
        return requests.get(url)


class AllBreeds:
    """Класс для получения всех пород"""
    def __init__(self):
        response = requests.get(base_breed_url)
        self.breeds = json.loads(response.text)['message']


@pytest.fixture()
def breeds():
    return AllBreeds().breeds


@pytest.fixture(autouse=True)
def client():
    """Фикситура для создания клиента"""
    return APIClient()
