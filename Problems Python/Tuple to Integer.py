""" Convert tuple to integer """
def tuple_to_int(tup):
    # convert each element to string using join() and iterate using for
    # convert to integer
    return int(''.join(str(x) for x in tup))


# input list elements
tuple_data = tuple(map(int, input('Enter tuple elements: ').split()))

# printing result
print(f'Tuple to integer conversion: {tuple_to_int(tuple_data)}')