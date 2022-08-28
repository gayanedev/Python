""" Check string is palindrome or no """
def is_palindrome(s):
    new_str = ''

    for elem in s:
        if elem.isalnum():
            new_str += elem.lower()

    if new_str == new_str[::-1]:
        return True
    return False


# input string
s_str = str(input("Enter the string: "))

print(is_palindrome(s_str))