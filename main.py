from data_structure.priority_queue import PriorityQueue, Entry
from data_structure.heap_sort import heap_sort
from heapq import heapify, heappop, heappush
import time
from random import randint


def timer(f):
    """ Декоратор для замера времениработы функции"""
    def tmp(*args, **kwargs):
        begin = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print("Время выполнения функции: {}".format(end - begin))
        return res
    return tmp


@timer
def heapsort(iterable):
    """ Пирамидальная сортировка с использованием минимальной кучи из модуля heapq"""
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]

@timer
def bubble_sorting(alist: list) -> list:
    """
    Сортировка пузырьком

    :type alist: object
    :param collection (list): Список для сортировки
    :return:
            collection (list): Отсортированный список
    """
    N = len(alist)
    for i in range(N - 1):
        swapped = True
        for j in range(N - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = False
        if swapped:
            break
    return alist


class Pair:
    """ Объект для макимальной кучи"""
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    # Переопределите оператор "меньше чем" __lt__ со знаком >, чтобы класс Pair работал с максимальной кучей.
    def __lt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f'({self.value}, {self.priority})'


def execute_application():

    """ Очередь с приоритетом
    queue = PriorityQueue()
    queue.insert("Помыть машину", 10)
    queue.insert("Сходить в кино", 7)
    queue.insert("Сделать домашнюю работу", 15)
    queue.insert("Погладить кота", 1)
    while not(queue.is_empty()):
        print(queue.delete())
    """

    """ Очередь с приоритетом из объектов Entry на основе минимальной кучи модуля heapq

    q = []

    heappush(q, Entry('A', 3))  # heappush is a method to add an
    heappush(q, Entry('B', 1))  # element
    heappush(q, Entry('C', 2))

    while q:
        next_item = heappop(q)  # heappop is a method to
        print(next_item)  # remove an element

    """

    """ Пирамидальная сортировка
    arr = [5, 3, 8, 12, 1, 0, 9]
    heap_sort(arr) # 12, 9, 8, 3, 1, 0, 5
    print(arr)
    """

    """ Максимальная куча на модуле heapq. Достаточно просто переопределить метод __lt__ в хранимом кучей объекте.
    # строит максимальную кучу пар
    pq = [Pair(7, 0), Pair(3, 3), Pair(9, 4), Pair(4, 1), Pair(6, 2), Pair(1, 5)]
    heapify(pq)

    # работает до тех пор, пока максимальная куча не станет пустой
    while pq:
        # вывести следующий максимальный элемент из кучи
        print(heappop(pq))
        
    """



if __name__ == "__main__":
    execute_application()
