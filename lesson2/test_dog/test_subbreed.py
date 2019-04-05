"""
Тестируем subbreed

"""

import pytest
from _datetime import datetime


LIST_OF_BREED = ["sss", "sss", "ssss"]

@pytest.mark.usefixtures("breeds")
@pytest.mark.usefixtures("client")
def test_sub_breed(breeds, client):
    """
    Проверяем страницы вида https://dog.ceo/api/breed/   название породы   /images/random
    Проверяем страницы вида https://dog.ceo/api/breed/   название породы   /images/
    Получаем список всех изображений для данной породы
    Проверяем, что по random выдается только одно изображение и оно находится в списке всех
    """

    print(len(breeds))
    for breed, subs in breeds.items():
        print(breed)
        print("     ", subs)
        """Если sub не пустое, то идем на страницу с породами и получаем список подпород"""
        print(len(subs))
        if len(subs) != 0:
            check_url()

        """Потом все изображения"""
        """Потом случайное"""
        """Потом три """



@pytest.fixture(params=LIST_OF_BREED)
def test_data(request):
    return request.param


def test_not_2(test_data):
    print('test_data: %s' % test_data)
    assert test_data != 2

@pytest.mark.usefixtures("make_urls")
@pytest.mark.parametrize("start", LIST_OF_BREED)
def test_2(start, make_urls):
    print(start)


def check_url(url, client):
    """Базовые проверки - ответ, дата время """
    response = client.do_get(url)
    assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response.json(), dict)
# #        s = breed.
#         response = client.do_get('/'.join(["breed", breed, "list"]))
#  #       assert
#
#         assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
#         assert response.status_code == 200
#         assert response.headers["Content-Type"] == "application/json"
#         all_images = response.json()["message"]
#         response = client.do_get('/'.join(["breed", breed, "images/random"]))
#         assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
#         assert response.status_code == 200
#         assert response.headers["Content-Type"] == "application/json"
#         image = response.json()["message"]
#         assert isinstance(image, str)
#         assert image in all_images
#         count = len(all_images)
#         for i in range(1, count):
#             response = client.do_get('/'.join(["breed", breed, "images/random", str(i)]))
#             assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
#             assert response.status_code == 200
#             assert response.headers["Content-Type"] == "application/json"
#             multi_images = response.json()["message"]
#             assert len(multi_images) == i
#             for single_image in multi_images:
#                 print(single_image)
#                 assert single_image in all_images


