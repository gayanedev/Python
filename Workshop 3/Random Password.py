from random import randint

""" Random password generator """
def random_passwd(n):
    min_ascii = 33
    max_ascii = 126
    rand_pass = ''

    # iterate on elements of length
    for i in range(n):
        # generate an appropriate number of random characters,
        # adding each one to the end of result
        rand_char = chr(randint(min_ascii, max_ascii))
        rand_pass += rand_char

    # return the random password
    return rand_pass


# input password length
pass_len = int(input('Enter the password length: '))

# printing result
print(f'The random password: {random_passwd(pass_len)}')