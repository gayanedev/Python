""" Return triple of a list item """
def triple(item):
    """ Triple of a item """
    return 3*item


# list
lst = list(map(int, input("Enter elements: ").split()))

# apply triple() function to each item of the items list
triple_items_iterator = map(triple, lst)

# converting to list
triple_items = list(triple_items_iterator)

# result is a list containing the triple of each item
print(f'The triple of each item is {triple_items}')