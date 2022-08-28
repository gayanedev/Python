""" Return the maximum number of consecutive 1's in the array """
def find_max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for i in nums:
        if i == 1:
            count += 1
        else:
            count = 0

        max_count = max(count, max_count)
    return max_count


list_nums = list(map(int, input('Enter list elements: ').split()))

print(find_max_consecutive_ones(list_nums))