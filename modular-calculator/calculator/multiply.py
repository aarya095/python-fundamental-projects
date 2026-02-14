from calculator.operation import Operation

class Multiply(Operation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b