"""Integer test"""


def test_div():
    """Check div"""
    int1 = 5
    int2 = 20
    i = int1/int2
    print(i)
    assert int(int1/int2) == 0
