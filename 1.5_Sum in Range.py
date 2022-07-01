""" Calculate the sum of numbers in given range """
def sum_num(a, b):
    total_sum = 0

    while a <= b:
        total_sum += a
        a += 1
    return total_sum


begin = int(input('Enter the min value for the range: '))
end = int(input('Enter the max value for the range: '))

print(f'The sum of numbers: {sum_num(begin, end)}')