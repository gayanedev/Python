""" Check if element or number exists in the list """
def contain(lst, value):
    # initialize index and counter
    i = 0
    counter = 0
    while i < len(lst):
        # for each element check whether its equal to the value or not
        if lst[i] == value:
            # if found initialize counter to 1
            counter = 1
        i += 1
    return counter


list_data = list(map(int, input("Enter elements: ").split()))
item_val = int(input("Enter a item value: "))

# check if counter variable is set to 1
if contain(list_data, item_val) == 1:
    print(f'{item_val} is present in the list')
else:
    print(f'{item_val} is not present in the list')