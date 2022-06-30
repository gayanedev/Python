""" Find maximum value in the list """
def max(data):
    # initial maximum value
    max_val = data[0]
    i = 0

    while i < len(data):
        # for each iteration check if item bigger than maximum value
        if data[i] >= max_val:
            max_val = data[i]
        i += 1
    # return maximum value
    return max_val


# input list items
lst = list(map(int, input('Enter list items: ').split()))

print(f'List maximum value: {max(lst)}')