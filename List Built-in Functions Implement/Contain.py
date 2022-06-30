""" Check if element exist in the list or no """
def contain(data, val):
    is_exist = False

    for i in range(len(data)):
        # for each element check whether its equal to the value or not
        if data[i] == val:
            is_exist = True

    if is_exist:
        return f'{val} exist in the list'
    else:
        return f'{val} is not exist in the list'


lst = list(map(int, input('Enter list items: ').split()))
item = int(input('Enter item value: '))

print(contain(lst, item))