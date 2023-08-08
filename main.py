import random
from module_1 import *
import math

""" Способы тестирования кода проекта
    1. С помощью assert
    2. Разработка от тестирования
    3. Модульное тестирование
"""


def run_test_square():

    assert square(0) == 0
    assert square(1) == 1
    assert square(-1) == 1
    assert square(5) == 25
    assert square(-5) == 25
    print("Пройдено 5 тестов из 5")


def test_prime(cur_value, exp_value):
    if is_prime(cur_value) != exp_value:
        print(f"ERROR in is_prime({cur_value}), expected {exp_value}")
    else:
        print(f"Testing is_prime({cur_value}) completed successfully")


def run_test_prime():
    test_prime(5, True)
    test_prime(0, False)
    test_prime(1, False)
    test_prime(-5, False)
    test_prime(13, True)


if __name__ == '__main__':

    print(math.sqrt(9))


