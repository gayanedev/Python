""" Check whether a number is prime or not """
def is_prime(num):
    prime_flag = 0
    # if given number is greater than 1
    # check prime or no
    if num > 1:
        # iterate from 2 to n / 2
        for i in range(2, int(num/2) + 1):
            # if num is divisible by any number between 2 and n / 2, it is not prime
            if num % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        return False
    return False


""" Find the smallest prime number greater than given number """
def next_prime(num):
    # base case
    if num <= 1:
        return 2

    # initialize prime and found
    prime = num
    found = False

    # loop continuously until isPrime returns True for a number greater than n
    while not found:
        # for every iteration check next number
        prime = prime + 1

        if is_prime(prime):
            found = True
    # return prime number
    return prime


# input number
number = int(input('Enter a number: '))

# printing result
print(f'The smallest prime number greater than {number} is {next_prime(number)}')