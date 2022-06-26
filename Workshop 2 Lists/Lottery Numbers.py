import random

""" Generate lottery six numbers """
def lottery_six():
    # initialize an empty list to create 6 lucky numbers
    lottery_numbers = []

    # iterate six times to create 6 lucky numbers
    for i in range(0, 6):
        # generate random numbers
        number = random.randint(1, 49)
        # check if this number already in the list or not
        while number in lottery_numbers:
            # if it has, choose a new number instead
            number = random.randint(1, 49)
        # append unique numbers to our list
        lottery_numbers.append(number)

    # sort the list in ascending order
    lottery_numbers.sort()

    # return unique lottery numbers
    return lottery_numbers


# printing result
print(f'The six numbers generated for the lottery ticket: {lottery_six()}')
