""" Remove items from the list """
def remove_items(lst, value):
    # initialize index
    i = 0
    while i < len(lst):
        # for each element check whether its equal to the value or not
        if lst[i] == value:
            # remove the value of the item from the list
            lst.remove(value)
        i += 1
    # return list
    return lst


list_data = list(map(int, input("Enter elements: ").split()))
item_val = int(input("Enter a item value: "))

# printing result
print(f'The list after performing the remove operation is {remove_items(list_data, item_val)}')