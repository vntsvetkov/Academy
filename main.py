class Programmer:

    def __init__(self, name: str, age: int, gender: str,
                 language: str, company: str,
                 salary: float = 0, premium: float = 0):
        # assert isinstance(age, int), "Неверный тип данных в поле age"
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__language = language
        self.__company = company
        self.__salary = salary
        self.__premium = premium

    def __str__(self):
        return f"Имя: {self.__name} \n" \
               f"Возраст: {self.__age} \n" \
               f"Пол: {self.__gender} \n" \
               f"Язык программирования: {self.__language} \n" \
               f"Компания: {self.__company} \n" \
               f"Заработная плата: {self.__salary + self.__premium}"

    @property
    def name(self):
        """@SelfDocumentation"""
        return self.__name

    @name.setter
    def name(self, name: str):
        # Подумать над обработкой
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        """

        :param age:
        :return:
        """
        if isinstance(age, int):
            if 18 <= age <= 65:
                self.__age = age
            else:
                raise Exception("Возраст не подходит")
        else:
            raise Exception("Не подходит тип значения")
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    def __calc_premium(self, percent: float = 0):
        """

        :param percent:
        :return:
        """
        return self.__salary * percent / 100

    def get_premium(self):
        return self.__premium

    def set_premium(self, percent: float = 0):
        self.__premium = self.__calc_premium(percent)
        # self.__premium = self.__salary * percent / 100


def execute_application():
    '''
    try:
        programmer = Programmer("Иван", "34", "male", "Python", "Яндекс", 100000)
    except AssertionError as e:
        print(e)
    '''

    programmer = Programmer("Иван", 34, "male", "Python", "Яндекс", 100000)

    try:
        programmer.age = "45"
    except Exception as e:
        print(e)

    print(programmer.age)


if __name__ == "__main__":
    execute_application()