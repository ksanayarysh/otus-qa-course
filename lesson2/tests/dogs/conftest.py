"""Conftest """
import json
import requests
import pytest


@pytest.fixture()
def breeds():
    """Возвращаем все породы"""
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    return json.loads(response.text)['message']
