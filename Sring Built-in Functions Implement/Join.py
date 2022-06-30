""" Join list elements with a separator """
def join(data, sep):
    string = ''

    for i in range(len(data)):
        if i != len(data) - 1:
            string += str(data[i]) + sep
        else:
            string += str(data[i])
    return string


# input list items
lst = list(map(int, input('Enter list items: ').split()))

# input separator
str_sep = str(input('Enter separator: '))

print(join(lst, str_sep))