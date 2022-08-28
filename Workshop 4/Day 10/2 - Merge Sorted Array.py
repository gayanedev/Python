""" Merge nums1 and nums2 into a single array """
def merge(nums1, m, nums2, n):
    i = 0

    for x in range(len(nums1)):
        if i >= n:
            break

        if nums1[x] == 0:
            nums1[x] = nums2[i]
            i += 1
    return nums1.sort()


list_nums_1 = list(map(int, input('Enter first list elements: ').split()))
list_nums_2 = list(map(int, input('Enter second list elements: ').split()))

number_1 = int(input('Enter a number: '))