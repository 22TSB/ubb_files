def solve():
    list = [15, 20, 35, 40]
    key = list[0]
    op = input()
    for i in range(1, len(list)):
        if (op == "+"):
            print(list[i] + key)
        elif (op == "*"):
            print(list[i] * key)
        elif (op == "^"):
            print(list[i] ^ key)


solve()
