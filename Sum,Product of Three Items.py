""" Return sum of three numbers """
def addition(data1, data2, data3):
    return data1 + data2 + data3


""" Return product of three numbers """
def multiple(data1, data2, data3):
    return data1 * data2 * data3


# list 1
lst1 = list(map(int, input("Enter elements: ").split()))

# list 2
lst2 = list(map(int, input("Enter elements: ").split()))

# list 3
lst3 = list(map(int, input("Enter elements: ").split()))

# calculate the sum
result2 = list(map(addition, lst1, lst2, lst3))

# calculate the product
result1 = list(map(multiple, lst1, lst2, lst3))

# result is a list containing the sum/product of three lists
print(f'The sum of three lists is {result1} list.The product of three lists is {result2} list')