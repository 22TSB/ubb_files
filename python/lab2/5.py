def calculate(expr, x, y):
    expr = expr.replace(" ", "")
    numbers = []
    operators = []
    current = ""

    for c in expr:
        if c.isdigit():
            current += c
        else:
            if current:
                if current == "x":
                    numbers.append(x)
                elif current == "y":
                    numbers.append(y)
                else:
                    numbers.append(int(current))
                current = ""

            if c == "x":
                numbers.append(x)
            elif c == "y":
                numbers.append(y)
            else:
                operators.append(c)

    if current:
        numbers.append(int(current))

    i = 0
    while i < len(operators):
        if operators[i] == "*":
            numbers[i] *= numbers[i + 1]
            numbers.pop(i + 1)
            operators.pop(i)
        elif operators[i] == "/":
            if numbers[i + 1] == 0:
                return None
            numbers[i] /= numbers[i + 1]
            numbers.pop(i + 1)
            operators.pop(i)
        else:
            i += 1

    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "-":
            result -= numbers[i + 1]

    return result


def satisfies(condition, x, y):
    left, right = condition.split("=")
    a = calculate(left, x, y)
    b = calculate(right, x, y)

    return a is not None and b is not None and a == b


def solve():
    condition = input("Condition: ")
    numbers = [12, 36, 31, 42, 63]

    result = []

    for number in numbers:
        x = number // 10
        y = number % 10

        if satisfies(condition, x, y):
            result.append(number)

    print(result)


solve()
