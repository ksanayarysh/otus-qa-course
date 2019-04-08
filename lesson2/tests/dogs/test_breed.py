"""
Тестируем breed

"""

import pytest
import requests
import basic

BASE_URL = "https://dog.ceo/api"
END_POINTS = ["images", "images/random", "images/random/3"]


@pytest.mark.usefixtures("breeds")
@pytest.mark.parametrize("end_point", END_POINTS)
@pytest.mark.dogs
def test_breed_image(breeds, end_point):
    """
    Для каждой породы проверяем, что страница пород открывается,
    выбирается случайное изображение и три случайных изображения
    """
    for breed in breeds.keys():
        url = '/'.join([BASE_URL, "breed", breed, end_point])
        response = requests.get(url)
        basic.base_check(response)
