""" Calculate characters count in file """
def char_count(file):
    # initialize number of characters
    number_of_char = 0

    # iterate over all lines
    for line in file:
        # won't count /n as character
        line = line.strip("\n")
        number_of_char += len(line)
    return number_of_char


# open input file
input_file = open('Files/original_file.txt', 'r')

# printing result
print(f'The number of characters: {char_count(input_file)}')

# close input file
input_file.close()