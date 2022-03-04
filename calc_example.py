import operator


class Calc:
    def __init__(self):
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv,
            '*': operator.mul,
            '%': operator.mod,
        }

    def calc(self, pattern):
        pattern_list = pattern.split()
        pattern_operands = []

        for operand in pattern_list:
            if operand.isdigit():
                pattern_operands.append(int(operand))
            else:
                pattern_operands.append(self.operators.get(operand))

        operand_1, operator_custom, operand_2 = pattern_operands

        return operator_custom(operand_1, operand_2)


c = Calc()
print(c.calc('2 % 5'))
