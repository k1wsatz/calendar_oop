class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


class LoggingCalculator(Calculator):
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = super().add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def sub(self, a, b):
        result = super().sub(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def mul(self, a, b):
        result = super().add(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def div(self, a, b):
        result = super().add(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result

lc = LoggingCalculator()
print(lc.add(1, 2))
print(lc.sub(1, 2))
print(lc.mul(1, 2))
print(lc.div(1, 2))
print(lc.mul(1, 2))
print(lc.history)