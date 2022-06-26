""" Check whether a number is perfect or not """
def perfect_number(n):
    # initializing sum of numbers to 0
    num_sum = 0

    # iterate from 1 to n/2
    for i in range(1, n//2 + 1):
        # check whether each number is perfectly divisible by number
        if n % i == 0:
            # sum each divisible number
            num_sum += i

    # return True if it is a perfect number and False otherwise.
    return num_sum == n


# input number
number = int(input('Enter a number: '))

# printing result
print(f'The sum of all divisors: {perfect_number(number)}')