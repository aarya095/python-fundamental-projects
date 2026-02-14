from calculator.divide import Divide

def test_divide():
    instance = Divide(50,5)
    assert instance.execute() == 10

def test_divide_negative_numbers():
    instance = Divide(-50,-5)
    assert instance.execute() == 10

def test_divide_one_negative_number():
    instance = Divide(50,-5)
    assert instance.execute() == -10