import math


def square(number: int) -> int:

    return number ** number


# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
def is_prime(number: int) -> bool:

    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
