""" Calculate count the frequencies in a list using dictionary """
def count_frequencies(lst):
    # initialize an empty dictionary
    freq_dict = {}

    # iterate over all elements in list
    for num in lst:
        # check if number exist in dictionary
        # if exists increase by one
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict


# input list elements
list_data = list(map(int, input('Enter elements: ').split()))

# printing result
print(count_frequencies(list_data))
