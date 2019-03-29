"""String tests """


def test_string1():
    """Copies string and ensures that lengths of new and source string are equal """
    string1 = 'Hello'
    string2 = 'world'
    string3 = string1 + ' ' + string2
    assert len(string3) == len(string1) + len(string2) + 1
