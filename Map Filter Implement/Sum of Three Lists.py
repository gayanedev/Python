""" Map function to calculate the sum of three list items """
def map3(func, data1, data2, data3):
    lst = []

    if len(data1) == len(data2) == len(data3):
        for i in range(len(data1)):
            lst.append(func(data1[i], data2[i], data3[i]))
        return lst
    raise ValueError('The lengths of the lists are not equal')

def sum(data1, data2, data3):
    """ Calculate sum of three items """
    return data1 + data2 + data3


# input three lists items
lst1 = list(map(int, input('Enter first list items: ').split()))
lst2 = list(map(int, input('Enter second list items: ').split()))
lst3 = list(map(int, input('Enter third list items: ').split()))

print(f'The sum of three lists: {map3(sum, lst1, lst2, lst3)}')