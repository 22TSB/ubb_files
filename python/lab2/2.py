def palin(n):
    inv = 0
    while (n):
        ci = n % 10
        inv = inv * 10 + ci 
        n //= 10
    return inv

list = [12, 21, 34, 43, 56]
cnt = 0

for i in range(len(list)):
    pi = palin(list[i])
    for j in range(i + 1, len(list)):
        if (pi == list[j]):
            cnt += 1

print(cnt)
