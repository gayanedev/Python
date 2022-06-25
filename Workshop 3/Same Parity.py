""" Get the arguments that are divisible by n """
def same_parity(n, *args):
    return [i for i in args if i % n == 0]


print(same_parity(3, 1, 2, 3, 4, 5, 6))