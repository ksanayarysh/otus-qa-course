"""Set tests"""


def test_set():
    """Check that double value is eliminated"""
    words = ['hello', 'daddy', 'hello', 'mum']
    set_word = set(words)
    print(set_word)
    assert len(set_word) == len(words) - 1


def test_set2():
    """Check length of union equals sum of their lengths - len of intersection"""
    set1 = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
    set2 = {'1', '2', '3', '4', '5'}
    result_set = set1.union(set2)
    result_length = len(set1) + len(set2) - len(set1.intersection(set2))
    print(result_set)
    print(len(result_set))
    assert len(result_set) == result_length
