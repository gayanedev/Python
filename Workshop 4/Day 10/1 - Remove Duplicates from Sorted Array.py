""" Return the length of the array after removing all duplicate entries
    perform this in O(1) extra space,so have to do the operation in-place """
def remove_duplicates(nums):
    previous = nums[0]
    length = 1
    index = 1

    if len(nums) == 0:
        return 0

    for i in range(1, len(nums)):
        if previous != nums[i]:
            length += 1
            previous = nums[i]
            nums[index] = nums[i]
            index += 1
    return length


list_nums = list(map(int, input('Enter list elements: ').split()))

print(remove_duplicates(list_nums))