""" Calculate sum of all the multiples of 3 or 5 below 1000 """
def multiples():
    mul_sum = 0

    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            mul_sum += i
    return mul_sum


print(multiples())