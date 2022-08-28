""" Calculate the difference between the sum and product of the digits """
def digits_product_sum(num):
    # initialize total sum and product
    total = 0
    product = 1

    while num > 0:
        # each digit of the number
        dig = num % 10
        # product of the digits
        product *= dig
        # sum of the digits
        total += dig
        num = num // 10
    # return subtraction
    return product - total


# input number
number = int(input("Enter a number:"))

# printing result
print(f'Subtracting the sum and product of digits: {digits_product_sum(number)}')