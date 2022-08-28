""" Capitalize the first letter of each word in a string """
def capitalize_word(string):
    # initialize result
    result = ''
    # split the string and get words in a list
    list_of_words = string.split()

    # iterate over all elements in list
    for elem in list_of_words:
        # capitalize first letter of each word and add to a string
        if len(result) > 0:
            result += ' ' + elem[0].upper() + elem[1:]
            # elem.capitalize()
        else:
            result = elem[0].upper() + elem[1:]
    return result


# open input and output file
input_file = open('Files/original_file.txt', "r")
output_file = open('Files/capitalize_file.txt', "w")
# get input file content
content = input_file.readlines()

# iterate over all lines in content
for line in content:
    # capitalize each line
    cap_line = capitalize_word(line)
    # save line in output file
    output_file.write(f'{cap_line}\n')

# close output file
output_file.close()