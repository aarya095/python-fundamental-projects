from calculator.multiply import Multiply

def test_multiply():
    instance = Multiply(3,5)
    assert instance.execute() == 15

def test_multiply_negative_numbers():
    instance = Multiply(-3,-5)
    assert instance.execute() == 15

def test_multiply_one_negative_number():
    instance = Multiply(-3,5)
    assert instance.execute() == -15