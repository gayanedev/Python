""" Find First and Last Position of Element in Sorted Array """
def search_range(nums, target):
    first_last = [-1, -1]

    for i in range(len(nums)):
        if nums[i] == target:
            if first_last[0] == -1:
                first_last[0] = i
            first_last[1] = i
    return first_last


list_nums = list(map(int, input('Enter list elements: ').split()))
num_target = int(input('Enter target: '))

print(search_range(list_nums, num_target))