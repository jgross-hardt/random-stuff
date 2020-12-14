class Expr:
    def __init__(self, value):
        self.value = bool(value)

    def __add__(self, other):
        return Expr(self.value or other.value)

    def __mul__(self, other):
        return Expr(self.value and other.value)

    def __str__(self):
        return str(int(self.value))

    def __repr__(self):
        return str(int(self.value))

    def __invert__(self):
        return Expr(not self.value)

    def __eq__(self, other):
        return Expr(self.value == other.value)

    def __ne__(self, other):
        return Expr(self.value != other.value)


def evaluate(expr, variables):
    temp = {}
    for k in variables:
        if k in globals():
            temp[k] = globals()[k]
        globals()[k] = variables[k]

    result = eval(expr)

    for k in variables:
        globals().pop(k)
    for k in temp:
        globals()[k] = temp[k]
    return result


def wertetabelle(variablestring, expr):
    variables = {}
    for e in variablestring:
        if e != " " and e != "," and e not in variables:
            variables[e] = Expr(0)
    for k in variables:
        print(k, end=" ")
    print("| result")
    print(("--" * len(variables)) + "--------")
    for i in range(2 ** len(variables)):
        x = len(variables) - 1
        for k in variables:
            variables[k] = Expr(1 if (2 ** x & i) else 0)
            print(1 if (2 ** x & i) else 0, end=" ")
            x -= 1
        print("|", end=" ")
        print(evaluate(expr, variables))
    print()


while True:
    wertetabelle(input("Enter variables: "), input("Enter expression: "))
