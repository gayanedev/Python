""" Map function to calculate the power of every base number """
def map2(func, data1, data2):
    lst = []

    for i in range(len(data1)):
        lst.append(func(data1[i], data2[i]))
    return lst

def pow(base, exp):
    """ Find the power of the base number to the provided exponent """
    return base ** exp

def is_positive(base):
    """ Check base is positive or no """
    # return True if positive and False for negative values
    return base >= 0

def filter2(func, data1):
    """ Filter negative values from the list """
    lst = []
    for i in range(len(data1)):
        if func(data1[i]):
            lst.append(data1[i])
    return lst


# input base list items
base_lst = list(map(int, input('Enter base list items: ').split()))

# input exponent list items
exp_lst = list(map(int, input('Enter exponent list items: ').split()))

print(f'The power of each item on the list: {map2(pow, filter2(is_positive, base_lst), exp_lst)}')
