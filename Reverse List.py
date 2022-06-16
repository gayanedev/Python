""" Reverse a List """
def reverse(lst):
    # initial first and last items
    i = 0
    j = len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    # return reversed list
    return lst


list_data = list(map(int, input("Enter elements: ").split()))

# printing the answer
print(f'The list after performing the reverse operation is {reverse(list_data)}')