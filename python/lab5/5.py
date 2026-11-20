from functools import reduce

list = [15, 3, 88, 42, 17]

def find_max(nums):
    reduce_list = reduce(lambda a, b: a if a > b else b, nums)
    return reduce_list

print(find_max(list))
