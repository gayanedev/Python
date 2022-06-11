""" Find the two largest numbers among the three input numbers and calculate sum of squares """
def sum_of_two_squares(num1, num2, num3):
    """ Find the two largest numbers among the three input numbers """
    if num2 >= num3 and num1 >= num3:
        l_num1, l_num2 = num1, num2
    elif num2 >= num1 and num3 >= num1:
        l_num1, l_num2 = num2, num3
    else:
        l_num1, l_num2 = num1, num3

    # return the sum of the squares of these two numbers
    return (l_num1**2) + (l_num2**2)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# printing the answer
print(f'Sum of squares is {sum_of_two_squares(a, b, c)}')
