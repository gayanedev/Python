""" Return True if any value appears at least twice in the array and return false if every element is distinct """
def contains_duplicate(nums):
    new_nums = []

    for i in nums:
        if i not in new_nums:
            new_nums.append(i)
        else:
            return True
    return False


list_nums = list(map(int, input('Enter list elements: ').split()))

print(contains_duplicate(list_nums))