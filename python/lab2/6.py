def same(a, b):
    return a % 10 == b // 10

list = [89, 95, 54, 43, 33, 25, 51]
leng = 0
nleng = 0
idxStart = 0
idxEnd = 0
for i in range(0, len(list) - 1):
    if (same(list[i], list[i + 1])):
        leng += 1
    elif (leng > nleng):
        nleng = leng
        idxStart = idxEnd
        idxEnd = i

for i in range(idxStart, idxEnd + 1):
    print(list[i])
