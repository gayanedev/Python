""" Contain function to check if element exist in the list or no """
def contain(data, val):
    is_contain = False

    for i in range(len(data)):
        # for each element check whether its equal to the value or not
        if data[i] == val:
            is_contain = True

    if is_contain:
        return f'{val} exist in the list'
    else:
        return f'{val} is not exist in the list'


lst = list(map(str, input('Enter list items: ').split()))
item = str(input('Enter item value: '))

print(contain(lst, item))