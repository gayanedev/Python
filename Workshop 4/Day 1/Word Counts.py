""" Calculate count of each word """
def word_count(content):
    # initialize an empty dictionary
    word_dict = {}  # or dict()

    # iterate over all lines
    for line in content:
        words = line.split()

        # iterate over all elements in list
        for word in words:
            # check if word exist in dictionary
            # if exists increase by one
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    # return word dictionary
    return word_dict


# open input file
input_file = open('Files/original_file.txt', 'r')
# get input file content
file_content = input_file.readlines()

# printing result
print(word_count(file_content))

# close input file
input_file.close()