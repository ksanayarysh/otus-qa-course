"""Test tuple"""


def test_city_tuple(get_city):
    """Check the city we want to visit is in our roadmap"""
    cities = ('Moscow', 'Novosibirsk', 'Sochi', 'Magadan', 'Ekat')
    my_city = get_city
    assert my_city in cities
