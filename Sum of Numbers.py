""" Calculate the sum of numbers in a given range """
def sum_of_numbers(begin, end):
    """ Computing sum of numbers from begin to end """
    # initialize total sum to 0
    total_sum = 0

    # base case: if first number bigger than second replace second with first and first with second
    if begin > end:
        begin, end = b, a

    while begin <= end:
        # update the total sum by adding the next term
        total_sum += begin
        begin += 1
    return total_sum


a = int(input("Enter a min number: "))
b = int(input("Enter a max number: "))

# printing the answer
print(f'Sum of natural numbers from {a} to {b} is {sum_of_numbers(a, b)}')
