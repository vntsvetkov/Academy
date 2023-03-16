class Programmer:

    name: str
    age: int
    gender: str
    language: str
    company: str

    def __init__(self, name: str, age: int, gender: str,
                language: str, company: str = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.language = language
        self.company = company

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Пол: {self.gender} \n" \
               f"Язык программирования: {self.language} \n" \
               f"Компания: {self.company}"



def execute_application():
    pass


if __name__ == "__main__":
    execute_application()