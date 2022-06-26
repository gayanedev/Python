""" Check if list is sorted or not """
def is_sorted(lst):
    flag = 0

    # iterate over the elements
    for i in range(len(lst) - 1):
        # element is bigger than the element after that
        # the list is not sorted
        if lst[i] > lst[i + 1]:
            flag = 1

    return flag


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
if not is_sorted(list_data):
    print('Yes, List is sorted')
else:
    print('No, List is not sorted')