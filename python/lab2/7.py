def cmmmmc(a, b):
    ca = a
    cb = b
    while(b):
        r = a % b
        a = b
        b = r
    return (ca * cb) // a


def solve():
    list = [10, 12, 14, 15, 20]
    start = int(input())
    end = int(input())
    num = list[start]
    for i in range(start + 1, end + 1):
        num = cmmmmc(num, list[i])     
    print(num)


solve()
