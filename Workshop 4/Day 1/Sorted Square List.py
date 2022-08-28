""" Squaring each element and sorting new list """
def square(lst):
    # initialize an empty list
    sqr_lst = []

    # iterate over all elements in list
    for item in lst:
        # square each number and append to a new list
        sqr_lst.append(item**2)
    # return sorted new list
    return sorted(sqr_lst)


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
print(f'Squaring list: {square(list_data)}')