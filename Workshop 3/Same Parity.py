""" Get the arguments that are divisible by n """
def same_parity(n, *args):
    return [i for i in args if i % n == 0]


lst = list(map(int, input('Enter list items: ').split()))
num = int(input('Enter a item value: '))

print(same_parity(num, *lst))