""" Remove every third character from string """
def del_third_char(string):
    new_str = string[0]

    # iterate over all string length
    for i in range(len(string)):
        if i % 3 != 0:
            new_str += string[i]
    return new_str


# input string
s = str(input('Enter the string: '))

# printing result
print(del_third_char(s))