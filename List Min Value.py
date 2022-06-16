""" Find Minimum value from the given list """
def min_value(lst):
    # initial the min to the first element
    min_val = lst[0]
    i = 0
    while i < len(lst):
        # for every element check if its smaller than min value
        if lst[i] < min_val:
            # assign the min value to the lst[i] value
            min_val = lst[i]
        i += 1
    # return minimum value
    return min_val


list_data = list(map(int, input("Enter elements: ").split()))

# printing the answer
print(f'The minimum value in the list is {min_value(list_data)[0]}')