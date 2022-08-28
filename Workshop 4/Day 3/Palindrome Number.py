""" Check number is palindrome or no """
def is_palindrome(x):
    revs_number = 0
    num = x
    while x > 0:
        remainder = x % 10
        revs_number = (revs_number * 10) + remainder
        x = x // 10

    return num == revs_number


# input number
number = int(input("Enter the number: "))

print(is_palindrome(number))
