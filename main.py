class Human:
    # Статическая переменная класса
    __AGE = 18

    def __init__(self, name: str = None, age: int = None):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def __str__(self):
        return f"Имя: {self.__name}, возраст: {self.__age}"

    def __repr__(self):
        return f"Класс: {Human.__name__}, ..."

    def info(self) -> str:
        return f"Имя: {self.__name}, возраст: {self.__age}"

    @classmethod
    def create_human_from_file(cls, path: str):
        with open(path, "r", encoding="utf-8") as file:
            name = file.readline().rstrip("\n")
            age = int(file.readline().rstrip("\n"))
            obj = cls(name, age)
        return obj

    @staticmethod
    def read_from_file(path: str) -> tuple:
        with open(path, "r", encoding="utf-8") as file:
            name = file.readline().rstrip("\n")
            age = int(file.readline().rstrip("\n"))
            if age >= Human.__AGE:
                tpl = (name, age)
            else:
                raise Exception("Невозможно создать объект")
        return tpl


def execute_application():
    #human = Human("Вася", 26)
    #human = Human.create_human_from_file("humans/human.txt")
    human = Human()
    human.name = "Вася"
    human.age = 45
    print(human.info())
    print(repr(human))


if __name__ == "__main__":
    execute_application()