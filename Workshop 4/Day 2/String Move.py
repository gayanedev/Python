""" Cyclically shifts the given string to the right by the given amount """
def str_move(str, d):
    r_first = str[0: len(str) - d]
    r_second = str[len(str) - d:]

    # concatenate two parts together
    return r_second + r_first


# input string
string = str(input("Enter the string: "))
# input number
num = int(input("Enter shift amount: "))

# printing result
print(str_move(string, num))

