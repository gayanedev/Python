""" Reverse a list """
def reverse(data):
    i = 0  # initial first item index
    j = len(data) - 1  # initial last item index

    while i < j:
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
    # return reverse list
    return data


# input list items
lst = list(map(str, input('Enter list items: ').split()))

print(f'The reverse list: {reverse(lst)}')