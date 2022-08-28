""" Find an intersection of two arrays """
def intersection(nums1, nums2):
    new_arr = []

    for i in nums1:
        if i in nums2 and i not in new_arr:
            new_arr.append(i)
    return new_arr


# input first list elements
list_1 = list(map(int, input('Enter first list elements: ').split()))

# input second list elements
list_2 = list(map(int, input('Enter second list elements: ').split()))

print(f'Intersection of two arrays: {intersection(list_1, list_2)}')