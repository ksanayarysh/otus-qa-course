"""Проверяем, что для всех подпород показывается список и изображения"""

import json
from datetime import datetime
import requests
import pytest


def get_locations_list():
    """Формируем список всех доступных подпород для всех пород"""
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    breeds = json.loads(response.text)['message']
    subs_list = []
    for breed, subs in breeds.items():
        if subs:
            subs_list.append("/".join(["breed", breed, "list"]))
    return subs_list


LOCATIONS = get_locations_list()


@pytest.mark.parametrize('location', LOCATIONS)
@pytest.mark.usefixtures("breeds")
def test_check_url(location, client):
    """
    Получаем список подподрок
    Базовые проверки - ответ, дата время для подпород
    """
    check_url(location, client)


def check_url(url, client):
    """Базовые проверки - ответ, дата время """
    response = client.do_get(url)
    assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response.json(), dict)


IMAGES = ["breed/hound/afghan/images",
          "breed/hound/afghan/images/random",
          "breed/hound/afghan/images/random/3"]


@pytest.mark.parametrize("image", IMAGES)
@pytest.mark.usefixtures("client")
def test_images(client, image):
    """Проверяем для подпороды все изображения, случайные и три случайных"""
    check_url(image, client)
