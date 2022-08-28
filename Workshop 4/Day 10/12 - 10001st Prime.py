""" Check the number is prime or no """
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


def find_10001st_prime(n):
    prime = 1
    count = 0

    while True:
        if is_prime(prime):
            count += 1
            if count == n:
                return prime
        prime += 1

    # while count < 10001:
    #     prime += 1
    #     if is_prime(prime):
    #         count += 1
    # return prime


# input number
number = int(input('Enter a number: '))

print(find_10001st_prime(number))