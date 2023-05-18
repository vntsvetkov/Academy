from collections import deque

from data_structure.queue import Queue
from data_structure.deque import Deque
from data_structure.linkedList import LinkedList


def execute_application():

    # Демонстрация связного списка
    link_list = LinkedList()
    link_list.add_first(1)
    link_list.add_first(2)
    link_list.add_last(3)
    link_list.add_last(4)

    # Итерация по всем элементам списка через метод items()
    # for item in link_list.items(): print(item)

    print(link_list.remove_last())
    print(link_list.remove_last())
    print(link_list.remove_last())
    print(link_list.remove_last())

    # Демонстрация очереди
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())


if __name__ == "__main__":
    execute_application()
