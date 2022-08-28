""" Find odd numbers in given range """
def odd_nums(start, end):
    # initialize list
    odd_lst = []

    # iterating each number in list
    for num in range(start, end + 1):
        # check number is odd
        if num % 2 != 0:
            odd_lst.append(num)
    return odd_lst


# input start
range_start = int(input("Enter the start of range: "))
# input end
range_end = int(input("Enter the end of range: "))

# printing result
print(f'Odd numbers in given range: {odd_nums(range_start, range_end)}')
