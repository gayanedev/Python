""" Tail Recursion solution to find the nth term in Fibonacci sequence """
def fib_tail_rec(n_terms, first=0, second=1):
    """ Tail recursive function to calculate nth number """
    if n_terms == 0:
        return first
    if n_terms == 1:
        return second
    # recursively call the same function n-1 times and correspondingly change the values of first and second
    return fib_tail_rec(n_terms - 1, second, first + second)


# input number of terms
number_terms = int(input("Enter the number of terms in the sequence: "))

# printing the answer
print(f'The sum of {number_terms} terms are {fib_tail_rec(number_terms)}')