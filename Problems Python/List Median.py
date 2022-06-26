""" Calculate the median of a list """
def median(lst):
    length = len(lst)
    # number in the middle
    half = length // 2
    # sorted list
    sort_list = sorted(lst)
    # the length of the list is even
    if not (length % 2):
        # the median is the average of the two middle elements
        list_median = (sort_list[half - 1] + sort_list[half]) / 2.0
        return list_median
    else:
        # the length of the list is odd
        # the median is the middle element
        list_median = sort_list[half]
        # return list median
        return list_median


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
print(f'The median of the list: {median(list_data)}')