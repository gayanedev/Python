""" Calculate the sum of numbers in file """
def num_sum(line):
    # initialize total
    total = 0

    # iterate over all elements
    for num in line:
        # check if number or no
        if num.isdigit():
            total += int(num)
    return total


# open input file
input_file = open('Files/numbers.txt', 'r')
# get input file content
content = input_file.read()

# printing result
print(f'The sum is: {num_sum(content)}')

# close input file
input_file.close()