"""Test dict"""


def test_dict_key_value():
    """Ensure that number of keys is equal to number of values in dict"""
    my_dict = {a: a ** 2 for a in range(7)}
    keys_count = my_dict.keys()
    values_count = my_dict.values()
    print(keys_count)
    print(values_count)
    assert len(keys_count) == len(values_count)
