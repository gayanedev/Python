""" Find minimum value in the list """
def min(data):
    # initial minimum value
    min_value = data[0]
    i = 0

    while i < len(data):
        # for each iteration check if item smaller than minimum value
        if data[i] <= min_value:
            min_value = data[i]
        i += 1
    # return minimum value
    return min_value


# input list items
lst = list(map(int, input('Enter list items: ').split()))

print(f'List minimum value: {min(lst)}')