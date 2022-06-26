""" Remove Duplicates from the list """
def remove_duplicate(lst):
    # initializing empty list
    res = []

    # iterate over the elements
    for i in lst:
        if i not in res:
            # add items that are not in the new list
            res.append(i)

    # return list without duplicates
    return res


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
print(f'The list after removing duplicates: {remove_duplicate(list_data)}')