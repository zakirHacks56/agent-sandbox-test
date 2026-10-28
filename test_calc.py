from calc import add


def test_add_negative():
    assert add(-2, 3) == 1


def test_add_positive():
    assert add(2, 3) == 5
