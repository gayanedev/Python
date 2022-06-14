""" Recursion solution to find the value of the Pascal triangle member """
def pascal_triangle(row, col):
    """ Find the value of the Pascal triangle member """
    # if the column value bigger than row value return error
    if col > row:
        return 'error'
    # if the value of the column is equal to 0 or equal to the value of the row return 1
    elif col in (0, row):
        return 1
    else:
        # the elements of the Pascal triangle are equal to the sum of the two adjacent elements in the preceding row
        return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)


# input the value of row and column
row = int(input("Enter row number: "))
column = int(input("Enter column number: "))

# printing the answer
print(f'The value of the Pascal triangle member is {pascal_triangle(row, column)}')
