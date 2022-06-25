""" Finding all divisors of a number """
def get_divisors(n):
    # initializing empty list
    divisor_lst = []

    # iterate from 1 to n/2
    for i in range(1, n//2 + 1):
        # check whether each number is perfectly divisible by number
        if n % i == 0:
            # add elements that are divisor of a number
            divisor_lst.append(i)
    divisor_lst.append(n)

    # return list of number divisors
    return divisor_lst


# input number
number = int(input('Enter a number: '))

# printing result
print(f'All divisors of a number: {get_divisors(number)}')
