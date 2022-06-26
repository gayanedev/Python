""" Remove Punctuations """
def remove_punctuation(sequence):
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""

    for char in sequence:
        # check if it not exists in the punctuation list
        if char not in punctuations:
            no_punct += char
    return no_punct


""" Check sequence palindrome or not """
def palindrome_seq(sequence):
    # remove punctuations from sequence
    seq = remove_punctuation(sequence)
    # convert the sequence to lowercase
    seq_low = seq.lower()
    # string to list
    lst = seq_low.split()

    # check if the list and reverse list is equal or not
    if lst == lst[::-1]:
        return True
    return False


# input sequence
seq = str(input('Enter a sequence: '))

# printing result
if palindrome_seq(seq):
    print('It is a palindrome sequence')
else:
    print('It is not a palindrome sequence')