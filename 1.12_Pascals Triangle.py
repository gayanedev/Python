""" Recursion solution to find the value of the Pascals triangle member """
def pascal_triangle(row, col):
    if col > row:
        raise ValueError('Column value out of range')

    if col in (0, row):
        return 1

    # each element of Pascal's triangle is equal to the sum of the two elements of the previous row
    return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)


# input row and column values
row = int(input('Enter row: '))
column = int(input('Enter column: '))

print(f'Tha value of the Pascal triangle member: {pascal_triangle(4, 3)}')
