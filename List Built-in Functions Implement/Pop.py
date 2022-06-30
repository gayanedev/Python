""" Pop the item by index and return value as a result """
def pop(data, i=None):
    # if an index is not passed, pop the last item
    if i is None or i == len(data) - 1:
        pop_item = data[-1]
        pop_lst = data[:-1]
    elif i >= len(data) or 0 > i < -len(data):
        raise ValueError('Pop index out of range')
    else:
        pop_item = data[i]
        pop_lst = data[:i] + data[i+1:]
    return pop_lst, pop_item


lst = list(map(int, input('Enter list items: ').split()))
index = int(input('Enter index: ')) or None

# return the value of the deleted index
print(f'The value of the pop index: {pop(lst, index)[1]}')

# return the list after deleted the current index item
print(f'The list after pop: {pop(lst, index)[0]}')
