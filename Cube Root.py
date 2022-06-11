""" Get absolute value """
def num_abs(n):
    if n > 0:
        return n
    return -n


""" Calculate the difference between square of new estimate and target number """
def guess_enough(value, target):
    # get absolute value
    if num_abs(value**3 - target) < 0.0001:
        return True
    return False


""" Calculate new estimate """
def improve(root, target):
    # calculate new estimate
    return ((target / root**2) + 2*root) / 3


""" Calculate number cube """
def sqrt(n):
    # initialize the value of root
    root = 1
    while not guess_enough(root, n):
        # each iteration, calculate a new estimate
        root = improve(root, n)
    return root


num = int(input("Enter number: "))

# printing the answer
print(f'The square root of {num} is {sqrt(num)}')
