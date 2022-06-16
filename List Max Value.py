""" Find Maximum value from the given list """
def max_value(lst):
    # initial the max to the first element
    max_val = lst[0]
    i = 0
    while i < len(lst):
        # for every element check if its grater than max value
        if lst[i] > max_val:
            # assign the max value to the lst[i] value
            max_val = lst[i]
        i += 1
    # return minimum value
    return max_val


list_data = list(map(int, input("Enter elements: ").split()))

# printing the answer
print(f'The maximum value in the list is {max_value(list_data)}')