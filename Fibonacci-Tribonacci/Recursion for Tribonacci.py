""" Recursion solution to find the nth term in f(n) = f(n - 1) + f(n - 2) + f(n - 3) sequence """
def trib_rec(n_terms):
    """ Recursive function to calculate nth number """
    # base case: if the number of terms is less than 3, return the same number
    if n_terms < 3:
        return n_terms
    # recursively call the same function
    return trib_rec(n_terms - 1) + trib_rec(n_terms - 2) + trib_rec(n_terms - 3)


# input number of terms
number_terms = int(input("Enter the number of terms in the sequence: "))

# printing the answer
print(f'The sum of {number_terms} terms are {trib_rec(number_terms)}')