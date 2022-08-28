""" Find an element that appears once """
def single_number(nums):
    if len(nums) == 1:
        return nums[0]

    for num in nums:
        if nums.count(num) == 1:
            return num


list_nums = list(map(int, input('Enter list elements: ').split()))

print(single_number(list_nums))

# second solution
def single_number_2(nums):
    lst = []

    for i in nums:
        if i not in lst:
            lst.append(i)
        else:
            lst.remove(i)
    return nums[0]