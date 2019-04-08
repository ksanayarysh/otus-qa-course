"""Базовые проверки"""
import json
from datetime import datetime
import requests


def check_case(url_first, url_second, sort):
    """Проверки, что в low case и upper case все ищется одинаково """
    response = requests.get(url_first + url_second.lower() + sort)
    base_check(response)
    breweries_by_city_count_low_case = len(json.loads(response.text))
    response = requests.get(url_first + url_second.capitalize() + sort)
    base_check(response)
    breweries_by_city_count_upper_case = len(json.loads(response.text))
    assert breweries_by_city_count_low_case == breweries_by_city_count_upper_case


def base_check(response):
    """Основные проверки"""
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert datetime.now().strftime("%d %b %Y") in response.headers["Date"]
