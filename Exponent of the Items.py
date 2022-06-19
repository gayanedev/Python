""" Check base positive or no """
def is_positive(base):
    return base >= 0


""" Find the power of the base number to the provided exponent """
def num_pow(base, exp):
    return base ** exp


# base list
base_list = list(map(int, input("Enter base elements: ").split()))

# exponent list
exp_list = list(map(int, input("Enter exponent elements: ").split()))

# filter() is used to filter out all negative values
lst = list(map(num_pow, filter(is_positive, base_list), exp_list))

# result is a list containing the power of each number
print(f'The power of each number is {lst}')