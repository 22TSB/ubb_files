def prim(n):
    d = 2
    nr = 1
    while (n > 1):
        p = 0
        while (n % d == 0):
            n //= d
            p += 1
        nr *= p + 1
        if (p > 0):
            if (p == 1):
                print(d, " ", d)
            print(d, " ", p)
        d += 1

prim(61)
