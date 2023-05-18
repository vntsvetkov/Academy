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
        self.__length = 0

    # add_first(item) - добавление элемента item в начало
    def add_first(self, item):
        self.__head = Node(item, self.__head)
        self.__length += 1
    # add_last(item) - добавление элемента item в конец

    def add_last(self, item):
        if self.__head is None:
            self.add_first(item)
        else:
            current_node = self.__head
            while current_node.link is not None:
                current_node = current_node.link
            current_node.link = Node(item)
            self.__length += 1
    # remove_first() - удаляет и возвращает первый элемент

    def remove_first(self):
        item = self.__head.data
        self.__head = self.__head.link
        self.__length -= 1
        return item

    # remove_last() - удаляет и возвращает последний элемент
    def remove_last(self):
        # FIXME: При удалении последнего элемента списка возвращается None
        if self.__head.link is None:
            self.remove_first()
        else:
            current_node = self.__head
            while current_node.link.link is not None:
                current_node = current_node.link
            item = current_node.link.data
            current_node.link = None
            self.__length -= 1
            return item
    # __len__ - возвращает количество элементов

    def __len__(self):
        return self.__length

    # items() - итератор, который последователно возвращает каждый элемент
