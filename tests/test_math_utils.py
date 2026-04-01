from src.app.math_utils import add_numbers


def test_add_integers():
    assert add_numbers(2, 3) == 5


def test_add_floats():
    assert add_numbers(1.5, 2.25) == 3.75
