from Time import Time


def execute_application():
    time1 = Time(10)
    time2 = Time(90)
    #time3 = time1 + time2
    #time4 = time1 + 100
    #time5 = time1 - 100
    #time6 = time1 - time2
    time1 += time2
    print(time1)
    time1 += 20
    print(time1)
    time1 -= time2
    print(time1)
    time1 -= 40
    print(time1)


if __name__ == "__main__":
    execute_application()