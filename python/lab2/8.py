def solve():
    list = [23, 41, 62]
    op = input()
    for i in list:
        if (op == "+"):
            print((i // 10) + (i % 10))
        elif (op == "*"):
            print((i // 10) * (i % 10))
        elif (op == "^"):
            print((i // 10) ^ (i % 10))


solve()
