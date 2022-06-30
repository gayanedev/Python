""" Remove items by value """
def remove_all(data, value):
    for i in data:
        # for each iteration check whether item is equal to the value or no
        # if equal remove the item from the list
        if i == value:
            data.remove(value)
    return data


lst = list(map(int, input('Enter list items: ').split()))
val = int(input('Enter a item value: '))

print(f'The list after removing: {remove_all(lst, val)}')