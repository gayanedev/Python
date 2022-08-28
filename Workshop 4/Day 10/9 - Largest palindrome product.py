""" Check number is palindrome or no """
def is_palindrome(num):
    possible_num = str(num)

    if possible_num == possible_num[::-1]:
        return True
    return False


"""" Find the largest palindrome made from the product of two 3-digit numbers """
def largest_palindrome():
    largest_pal = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j) and i * j > largest_pal:
                largest_pal = i * j
    return largest_pal


print(largest_palindrome())