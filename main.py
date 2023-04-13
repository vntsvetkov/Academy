from Time import Time


def execute_application():
    time1 = Time(65)
    time2 = Time(65)
    time3 = time1 + time2
    time4 = time1 + 100
    print(time3)
    print(time4)


if __name__ == "__main__":
    execute_application()