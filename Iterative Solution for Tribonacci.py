""" Iterative solution to find the nth term in f(n) = f(n - 1) + f(n - 2) + f(n - 3) sequence """
def trib_iter(n):
    """ Iterative function to calculate nth number """
    # initialize first three numbers as 0, 1 and 2
    first = 0
    second = 1
    third = 2
    n_terms = n

    if n_terms < 0:
        return "Input must be a positive integer"
    else:
        # use while loop to find the sum of the first three terms
        # and proceed with the series by interchanging the variables till number of terms is greater than 0
        while n_terms != 0:
            term = first + second + third
            first, second, third = second, third, term
            # decrement the value of n
            n_terms -= 1
        # return sum
        return f'The sum of {n} terms are {first}'


# input number of terms
number_terms = int(input("Enter the number of terms in the sequence: "))

# printing the answer
print(trib_iter(number_terms))