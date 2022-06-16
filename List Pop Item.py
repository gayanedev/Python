""" Delete the element in index i and return the value of the element as a result """
def pop_item(lst, i=None):
    # if an argument is not passed,delete the last item
    if i is None:
        lst = lst.pop(-1)
    else:
        # delete current index value
        lst = lst.pop(i)
    # return deleted value
    return lst


list_data = list(map(int, input("Enter elements: ").split()))
index = input("Enter a index:") or None

# printing the answer
print(f'The value of the deleted index is {pop_item(list_data, index)}')
