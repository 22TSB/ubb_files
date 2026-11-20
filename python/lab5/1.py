arr = [121, 324, 44, 897, 1331, 50]

def palindrom(n):
    cn = n
    inv = 0
    while n:
        dig = n % 10
        inv = inv * 10 + dig
        n //= 10
    return cn == inv

def mirrored_numbers(nums):
    filter_list = filter(palindrom, nums)
    map_list = map(lambda x: str(x), filter_list)
    return list(map_list)

print(mirrored_numbers(arr))
