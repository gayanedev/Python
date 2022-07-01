""" Map function to calculate the triple of each item """
def map2(func, data):
    lst = []

    for i in range(len(data)):
        lst.append(func(data[i]))
    return lst

def triple(data):
    """ Calculate the triple of the item """
    return 3 * data


# input list items
lst = list(map(int, input('Enter list items: ').split()))

print(f'The triple of each item on the list: {map2(triple, lst)}')