"""  Find the length of the last word in the string """
def length_of_last_word(s):
    word_array = s.split()

    return len(word_array[-1])


# input string
s_str = str(input("Enter the string: "))

print(length_of_last_word(s_str))