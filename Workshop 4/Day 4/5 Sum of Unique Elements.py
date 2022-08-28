""" Calculate sum of all the unique elements of number list """
def sum_of_unique(nums):
    total_sum = 0
    counts = {}

    for x in nums:
        if x in counts.keys():
            counts[x] += 1
        else:
            counts[x] = 1

    for (k, v) in counts.items():
        if v == 1:
            total_sum += k

    return total_sum


# input number list elements
num_lst = list(map(int, input('Enter num list elements: ').split()))

print(sum_of_unique(num_lst))