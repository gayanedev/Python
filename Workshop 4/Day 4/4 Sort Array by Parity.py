""" Move all the even integers at the beginning of the array followed by all the odd integers and return array """
def sort_array_by_parity(nums):
    even_arr = []
    odd_ar = []

    for i in nums:
        if i % 2 == 0:
            even_arr.append(i)
        else:
            odd_ar.append(i)
    return even_arr + odd_ar


# input num list elements
num_lst = list(map(int, input('Enter list elements: ').split()))

print(sort_array_by_parity(num_lst))