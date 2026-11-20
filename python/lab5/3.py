from functools import reduce

arr = [1, 2, 5, 6, 8, 9, 10]

def count_even(nums):
    filter_list = filter(lambda i: i % 2 == 0, nums)
    reduce_list = reduce(lambda acc, i: acc + 1, filter_list, 0)
    return reduce_list

print(count_even(arr))
