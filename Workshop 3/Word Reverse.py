""" Get the reverse of the word """
def word_reverse(str):
    rev_str = ''
    for i in str:
        # adding each letter at the beginning of the result
        rev_str = i + rev_str
    # return the reverse string
    return rev_str


# input word
word = str(input("Enter a word: "))

# printing result
print(f'Reverse word: {word_reverse(word)}')