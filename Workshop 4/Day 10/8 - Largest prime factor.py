import math

def is_prime(num):
    prime_flag = 0

    if num > 1:
        for i in range(2,  int(num//2) + 1):
            if num % i == 0:
                prime_flag = 1
                break
        if prime_flag == 1:
            return False
        return True
    return False


def largest_prime_factor(number):
    answer = []

    for i in range(3, int(math.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            answer.append(i)
    return max(answer)


print(largest_prime_factor(600851475143))