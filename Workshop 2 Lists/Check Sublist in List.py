""" Check if one list is a sublist of another """
def is_sublist(lst, sub_lst):
    is_sub = False

    for idx in range((len(lst) - len(sub_lst)) + 1):
        # check sublist in list
        if lst[idx: idx + len(sub_lst)] == sub_lst:
            is_sub = True
            break

    # return true or false
    return is_sub


# input list elements
lst_data = list(map(int, input('Enter list elements: ').split()))

# input sublist elements
sub_lst_data = list(map(int, input('Enter sublist elements: ').split()))

# printing result
print(is_sublist(lst_data, sub_lst_data))