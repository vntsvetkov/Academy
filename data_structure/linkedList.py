class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


"""
LinkedList или связный список – это структура данных. 
Связный список обеспечивает возможность создать двустороннюю очередь из каких-либо элементов. 
Каждый элемент такого списка считается узлом (Node). 
В каждом узле есть его значение, а также две ссылки – на предыдущий и на последующий узлы. 
То есть список «связывается» узлами, которые помогают двигаться вверх или вниз по списку. 
Из-за таких особенностей строения из связного списка можно организовать стек, очередь или двустороннюю очередь.
"""


class LinkedList:
    def __init__(self):
        self.__head = None

    # add_first(item) - добавление элемента item в начало
    # add_last(item) - добавление элемента item в конец
    # remove_first() - удаляет и возвращает первый элемент
    # remove_last() - удаляет и возвращает последний элемент
    # len - возвращает количество элементов
    # is_empty() - проверяет пустой ли список
    # items() - итератор, который последователно возвращает каждый элемент
