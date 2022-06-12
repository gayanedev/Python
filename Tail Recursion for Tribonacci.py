""" Tail Recursion solution to find the nth term in f(n) = f(n - 1) + f(n - 2) + f(n - 3) sequence """
def trib_tail_rec(n_terms, first=0, second=1, third=2):
    """ Tail recursive function to calculate nth number """
    if n_terms == 0:
        return first
    if n_terms == 1:
        return second
    if n_terms == 2:
        return third
    # recursively call the same function n-1 times and correspondingly change the values of first, second and third
    return trib_tail_rec(n_terms - 1, second, third, first + second + third)


# input number of terms
number_terms = int(input("Enter the number of terms in the sequence: "))

# printing the answer
print(f'The sum of {number_terms} terms are {trib_tail_rec(number_terms)}')