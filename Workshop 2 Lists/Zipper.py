""" Zip function """
def zipper(data1, data2):
    # check lists length are equal or no
    if len(data1) == len(data2):
        # initializing empty list
        zip_lst = []

        # iterate over the elements
        for i in range(len(data1)):
            zip_lst.append([data1[i], data2[i]])

        # return zipper list
        return zip_lst
    raise ValueError('Workshop 2 Lists are not equal')


# input first list elements
list1 = list(map(int, input('Enter first list elements: ').split()))

# input second list elements
list2 = list(map(int, input('Enter second list elements: ').split()))

# printing result
print(f'Zip list: {zipper(list1, list2)}')