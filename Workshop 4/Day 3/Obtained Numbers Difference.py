""" Calculate the difference between the squared sum of 100 numbers and the sum of squared 100 numbers """
def sum_difference(n):
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, n + 1):
        sum_of_squares += i ** 2
        square_of_sum += i

    square_of_sum = square_of_sum ** 2

    return square_of_sum - sum_of_squares


# input number
num_val = int(input("Enter number of value: "))

# printing the answer
print(sum_difference(num_val))