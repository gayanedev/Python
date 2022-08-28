""" Calculate the sum of even values in Fibonacci sequence """
def sum_even_val_fib():
    # initialize first two numbers as 1 and 1
    first, second = 1, 1
    total = 0

    # use while loop to find the sum of the first two terms
    # and proceed with the series by interchanging the variables till number of terms is smaller than four million
    while second < 4000000:
        term = first + second
        first, second = term, first

        # check even or no
        if second % 2:
            continue
        # calculate the sum of the terms
        total += second
    return total


# printing result
print(sum_even_val_fib())

