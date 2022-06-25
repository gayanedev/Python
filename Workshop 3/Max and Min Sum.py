""" Get the sum of the largest and smallest numbers of list """
def max_min_sum(lst):
    # max number
    max_num = max(lst)
    # min number
    min_num = min(lst)
    # return the sum of the max and min numbers
    return int(max_num + min_num)


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
print(f'The sum of minimum and maximum elements: {max_min_sum(list_data)}')