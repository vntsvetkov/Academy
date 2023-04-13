class Time:

    def __init__(self, value: int):
        self.__value = value

    @staticmethod
    def __format(time):
        return f"{time // 10}{time % 10}"

    @classmethod
    def create_time(cls, hour: int, minute: int, second: int):
        # TODO: перевести часы, минуты, секунды -> секунды
        pass

    def __str__(self):
        hour = self.__value // 3600 % 24
        minute = self.__value // 60 % 60
        second = self.__value % 60
        return f"{Time.__format(hour)}:" \
               f"{Time.__format(minute)}:" \
               f"{Time.__format(second)}"

