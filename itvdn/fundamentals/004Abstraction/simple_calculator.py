class Parser:
    def __init__(self) -> None:
        pass

    def parse(self, expression):
        a, op, b = tuple(expression.split(' '))
        return int(a), int(b), op


class Core:
    def __init__(self) -> None:
        self._parser = Parser()
        self._functions = {
            "+":  lambda a, b: a + b,
            "-":  lambda a, b: a - b,
            "/":  lambda a, b: a / b,
            "*":  lambda a, b: a * b
        }
    
    def calculate(self, expression):
        a, b, op, = self._parser.parse(expression)
        result = self._functions.get(op)(a, b)
        return result


class Interface:
    def __init__(self) -> None:
        self._core = Core()
    
    def run_calculator(self):
        while True:
            print('Enter yout expression: eg. "2 + 2"')
            expression = input()
            result = self._core.calculate(expression)
            print(f'Result: {result}')


if __name__ == '__main__':
    calculator = Interface()
    calculator.run_calculator()
