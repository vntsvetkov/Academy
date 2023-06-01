import datetime
import time


def func_log(file_log="log.txt"):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now()
            date_string = current_time.strftime('%d.%m %H:%M:%S')
            log_string = f"{str(func.__name__)} вызвана {date_string}\n"
            with open(file_log, "a", encoding="utf-8") as file:
                file.writelines(log_string)
            return func(*args, **kwargs)
        return wrapper
    return log_decorator


@func_log()
def func1():
    time.sleep(1)
    print("Привет из функции func1")


func1()