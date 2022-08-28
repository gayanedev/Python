def array_pair_sum(nums):
    res = 0

    nums.sort()

    for i in range(0, len(nums), 2):
        res += min(nums[i], nums[i + 1])
    return res


list_nums = list(map(int, input('Enter list elements: ').split()))

print(array_pair_sum(list_nums))