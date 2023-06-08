import time


def timer(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        return "Время выполнения функции: {}".format(end - begin)
    return wrapper


def null_decorator(func):
    return func


def split_decorator(symbol):
    def main_decorator(func):
        def wrapper(*args, **kwargs):
            original_result = func(*args, **kwargs)
            modified_result = original_result.split(symbol)
            return modified_result
        return wrapper
    return main_decorator


def upper_decorator(func):
    def wrapper(*args, **kwargs):
        original_result: str = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@timer
@split_decorator(symbol="I")
@upper_decorator
def main(n: int, flag=False) -> str:
    return "Hello from main function"[:n]


print(main(15))
