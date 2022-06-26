""" Get indexes of even elements from list """
def even_indexes(lst):
    # initializing empty list
    indexes = []

    # iterate on elements of length
    for i in range(len(lst)):
        # check element even or no
        if lst[i] % 2 == 0:
            # append the indexes of even elements to the list
            indexes.append(i)

    # return the list of indexes
    return indexes


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
print(f'Even elements indexes : {even_indexes(list_data)}')