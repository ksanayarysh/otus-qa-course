import pytest
import json
import requests
from datetime import datetime


def get_locations_list():
    """Формируем список всех доступных подпород для всех пород"""
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    breeds = json.loads(response.text)['message']
    subs_list = []
    for breed, subs in breeds.items():
        if len(subs) > 0:
            subs_list.append("/".join(["breed", breed, "list"]))
    return subs_list


LOCATIONS = get_locations_list()


@pytest.mark.parametrize('location', LOCATIONS)
def test_things(location):
    print(location)


@pytest.mark.parametrize('location', LOCATIONS)
@pytest.mark.usefixtures("breeds")
def test_check_url(location, client):
    """Базовые проверки - ответ, дата время """
    response = client.do_get(location)
    assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response.json(), dict)


def check_url(url, client):
    """Базовые проверки - ответ, дата время """
    response = client.do_get(url)
    assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response.json(), dict)




@pytest.mark.usefixtures("client")
def test_images(client):
    url = "breed/hound/afghan/images"
    check_url(url, client)
    url = "breed/hound/afghan/images/random"
    check_url(url, client)
    url = "breed/hound/afghan/images/random/3"
    check_url(url, client)
