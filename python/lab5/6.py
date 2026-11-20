from functools import reduce

nums = [120, 95, 88, -3, 102, 70]

def comp(n):
    if n >= 0 and n <= 100:
        return True
    return False

def normalize_and_sum(nums):
    valid_score = filter(comp, nums)
    normalized_score = map(lambda x: x / 100, valid_score)
    reduce_list = reduce(lambda acc, x: acc + x, normalized_score, 0) 
    return reduce_list

print(f"{normalize_and_sum(nums):.2f}")
