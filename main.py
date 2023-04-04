from figures import *
"""
Абстрактные классы.
Определяет общий интерфейс для набора подклассов.
Особенности:
1. Содержит абстрактные методы - методы без реализации
2. Нельзя создать экземпляр абстрактного класса
3. Класс наследник обязан переопределить все методы
которые описаны в абстрактном классе.
"""


def execute_application():
    rect = Rectangle(0, 0, 3, 4)
    print(rect.area())
    print(rect.perimetr())
    print(rect.area_by_diagonal())


if __name__ == "__main__":
    execute_application()