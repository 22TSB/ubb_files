def prime(n):
    d = 2
    nr = 1
    while(n > 1):
        p = 0
        while(n % d == 0):
            n //= d
            p += 1
        nr *= p + 1
        d += 1
        if d * d > n:
            d = n
    return nr == 2

n = int(input())

i = 1
while n > 0:
    if prime(i):
        print(i, end=' ')
        n -= 1
    i += 1
