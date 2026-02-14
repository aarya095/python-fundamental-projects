from calculator.add import Add

def test_add_positive_numbers():
    instance = Add(4,6)
    assert instance.execute() == 10

def test_add_negative_numbers():
    instance = Add(-4,-6)
    assert instance.execute() == -10

def test_add_negative_positive_numbers():
    instance = Add(-4,6)
    assert instance.execute() == 2