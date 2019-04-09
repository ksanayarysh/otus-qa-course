"""Тестирование сайта opencart"""


def test_open_cart(driver, get_url):
    """Открываем выбранный url выбранным драйвером"""
    driver.get("http://" + get_url + "/opencart/")
    assert driver.current_url == "http://" + get_url + "/opencart/"
