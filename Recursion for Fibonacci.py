""" Recursion solution to find the nth term in Fibonacci sequence """
def fib_rec(n_terms):
    """ Recursive function to calculate nth number """
    if n_terms == 0:
        return 0
    elif n_terms in (1, 2):
        return n_terms - 1
    # recursively call the same function
    return fib_rec(n_terms - 1) + fib_rec(n_terms - 2)


# input number of terms
number_terms = int(input("Enter the number of terms in the sequence: "))

# printing the answer
print(f'The sum of {number_terms} terms are {fib_rec(number_terms)}')