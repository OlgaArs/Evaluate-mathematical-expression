OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
              '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

def calc(formula: str) -> int:

    def simplification(formula_string: str) -> str:
        formula_string = formula_string.replace(' ', '')
        formula_string = formula_string.replace('--', '+')
        formula_string = formula_string.replace('+-', '-')
        formula_string = formula_string.replace('/-(', '/(0-1)/(')
        formula_string = formula_string.replace('*-(', '*(0-1)*(')
        formula_string = formula_string.replace('/-', '/(0-1)/')
        formula_string = formula_string.replace('*-', '*(0-1)*')
        formula_string = formula_string.replace('(-', '(0-')
        if formula_string[0] == '-':
            formula_string = '0'+formula_string
        return formula_string

    def parse(formula_string: str) -> float:
        number = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula: str) -> str:
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calculate(polish: str) -> int:
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calculate(shunting_yard(parse(simplification(formula))))


if __name__ == '__main__':
    assert calc("1 + 1") == 2
    assert calc("8/16") == 0.5
    assert calc("3 -(-1)") == 4
    assert calc("2 + -2") == 0
    assert calc("10- 2- -5") == 13
    assert calc("(((10)))") == 10
    assert calc("3 * 5") == 15
    assert calc("-7 * -(6 / 3)") == 14
