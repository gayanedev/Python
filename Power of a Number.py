""" Find Power of a Number """
def num_power(base, exp):
    """ Find exponent of a given number """
    # initialize result
    res = 1
    count = 0
    # using while loop to calculate the exponential value
    while count < abs(exp):
        if exp > 0:
            res = res * base
        elif exp < 0:
            res = res / base
        else:
            # base case: if exponent equal zero
            # the power of zero is one
            res = 1
        count += 1
    # return final result
    return res


base = int(input("Enter base : "))
exponent = int(input("Enter exponent : "))

# printing the answer
print(f'The Result of {base} Power {exponent} = {num_power(base, exponent)}')
