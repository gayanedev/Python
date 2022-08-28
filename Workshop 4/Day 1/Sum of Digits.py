""" Calculate sum of digits """
def digits_sum(num):
    # initialize total sum
    total = 0

    while num > 0:
        # each digit of the number
        dig = num % 10
        # sum of the digits
        total += dig
        num = num // 10
    # return total sum
    return total


# input number
number = int(input("Enter a number:"))

# printing result
print(f'The total sum of digits: {digits_sum(number)}')