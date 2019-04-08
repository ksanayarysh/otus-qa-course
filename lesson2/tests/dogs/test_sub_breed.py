"""Проверяем, что для всех подпород показывается список и изображения"""

import json
import requests
import pytest
import basic


BASE_URL = 'https://dog.ceo/api'


def get_locations_list():
    """Формируем список всех доступных подпород для всех пород"""
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    breeds = json.loads(response.text)['message']
    subs_list = []
    for breed, subs in breeds.items():
        if subs:
            subs_list.append("/".join([BASE_URL, "breed", breed, "list"]))
    return subs_list


LOCATIONS = get_locations_list()


@pytest.mark.parametrize('location', LOCATIONS)
@pytest.mark.dogs
def test_check_url(location):
    """
    Получаем список подподрок
    Базовые проверки - ответ, дата время для подпород
    """
    response = requests.get(location)
    basic.base_check(response)


IMAGES = ["breed/hound/afghan/images",
          "breed/hound/afghan/images/random",
          "breed/hound/afghan/images/random/3"]


@pytest.mark.parametrize("image", IMAGES)
@pytest.mark.dogs
def test_images(image):
    """Проверяем для подпороды все изображения, случайные и три случайных"""
    url = "/".join([BASE_URL, image])
    response = requests.get(url)
    basic.base_check(response)
