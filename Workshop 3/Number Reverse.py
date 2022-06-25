""" Get the reverse of the number """
def reverse_number(num):
    # initialize variable with 0
    reverse = 0

    # repeat this process until the number becomes 0
    while num != 0:
        # for every iteration get the last digit of the number
        last_digit = num % 10
        # multiply the variable by 10
        # add that last digit to the variable
        reverse = (reverse * 10) + last_digit
        # remove the last digit of the number
        num //= 10

    # return the reverse number
    return reverse


# input number
number = int(input('Enter a number: '))

# printing result
print(f'Reverse number: {reverse_number(number)}')