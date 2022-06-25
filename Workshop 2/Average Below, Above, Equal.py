""" Find the list of numbers below average, average and above average """
def below_above_equal(lst):
    # initializing empty list
    below, above, equal = [], [], []
    # calculate average
    average = sum(lst) / len(lst)

    # iterate over the elements
    for i in lst:
        if i < average:
            # append elements that are lower than average
            below.append(i)
        if i == average:
            # append elements that are equal to the mean
            equal.append(i)
        if i > average:
            # append items that are larger than average
            above.append(i)

    # return below, equal, above lists
    return average, below, equal, above


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
print(f'The average value of the numbers: {below_above_equal(list_data)[0]}')
print(f'List of below average numbers: {below_above_equal(list_data)[1]}')
if below_above_equal(list_data)[2]:
    print(f'Equal to the average number: {below_above_equal(list_data)[2]}')
print(f'List of above average numbers: {below_above_equal(list_data)[3]}')