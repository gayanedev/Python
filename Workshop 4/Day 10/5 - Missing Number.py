""" Return the only number in the range that is missing from the array """
def missing_number(nums):
    nums.sort()

    if nums[-1] == len(nums) - 1: return len(nums)

    for i in range(len(nums)):
        if nums[i] != i:
            return i


list_nums = list(map(int, input('Enter list elements: ').split()))

print(missing_number(list_nums))