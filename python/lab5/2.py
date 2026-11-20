from functools import reduce

arr = [1, 2, 3]

def sum_of_cubes(nums):
    reduce_list = reduce(lambda acc, x: acc + x**3, nums, 0)
    return reduce_list
    
print(sum_of_cubes(arr))
