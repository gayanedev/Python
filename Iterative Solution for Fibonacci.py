""" Iterative solution to find the nth term in Fibonacci sequence """
def fib_iter(n):
    """ Iterative function to calculate nth number """
    # initialize first two numbers as 0 and 1
    first = 0
    second = 1
    n_terms = n

    if n_terms < 0:
        return "Input must be a positive integer"
    else:
        # use while loop to find the sum of the first two terms
        # and proceed with the series by interchanging the variables till number of terms is greater than 0
        while n_terms > 0:
            term = first + second
            first, second = second, term
            # decrement the value of n
            n_terms -= 1
        # return sum
        return f'The sum of {n} terms are {first}'


# input number of terms
number_terms = int(input("Enter the number of terms in the sequence: "))

# printing the answer
print(fib_iter(number_terms))