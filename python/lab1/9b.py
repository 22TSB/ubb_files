def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))


def lsub(nums):
    start = 0
    best_start = 0
    best_len = 1
    length = 1

    for i in range(1, len(nums)):
        if same_digits(nums[i - 1], nums[i]):
            length += 1
        else:
            length = 1
            start = i

        if length > best_len:
            best_len = length
            best_start = start

    return nums[best_start:best_start + best_len]


list = [12, 21, 34, 43, 56, 65, 12, 21, 12]

print(lsub(list))
