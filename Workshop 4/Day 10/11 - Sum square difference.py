""" Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum """
def sum_square_difference():
    sum_square = 0
    n_list = list(range(1, 101))

    for i in n_list:
        sum_square += i ** 2
    square_sum = sum(n_list) ** 2

    return square_sum - sum_square


print(sum_square_difference())