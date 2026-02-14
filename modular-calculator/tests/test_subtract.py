from calculator.subtract import Subtract

def test_subtract():
    instance = Subtract(5,2)
    assert instance.execute() == 3

def test_subtract_negative_numbers():
    instance = Subtract(-5,2)
    assert instance.execute() == -7

def test_subtract_two_negative_numbers():
    instance = Subtract(-5,-2)
    assert instance.execute() == -3