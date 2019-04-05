"""
Тестируем breed

"""

import pytest
from _datetime import datetime


@pytest.mark.usefixtures("breeds")
@pytest.mark.usefixtures("client")
def test_breed_image(breeds, client):
    """
    Для каждой породы проверяем, что страница пород открывается,
    выбирается случайное изображение и три случайных изображения
    """
    for breed, subs in breeds.items():
        check_url('/'.join(["breed", breed, "images"]), client)
        check_url('/'.join(["breed", breed, "images/random"]), client)
        check_url('/'.join(["breed", breed, "images/random/3"]), client)


def check_url(url, client):
    """Базовые проверки - ответ, дата время """
    response = client.do_get(url)
    assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response.json(), dict)
