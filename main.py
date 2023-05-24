from data_structure.priority_queue import PriorityQueue, Entry
from data_structure.heap_sort import heap_sort
from heapq import heapify, heappop, heappush
from random import randint
from data_structure.max_heap import MaxHeap, Pair


def execute_application():

    """ Очередь с приоритетом (реализация на списках)

    queue = PriorityQueue()
    queue.insert("Помыть машину", 10)
    queue.insert("Сходить в кино", 7)
    queue.insert("Сделать домашнюю работу", 15)
    queue.insert("Погладить кота", 1)
    while not(queue.is_empty()):
        print(queue.delete())

    """

    """ Очередь с приоритетом из объектов Entry (реализация на минимальной куче модуля heapq)

    q = []

    heappush(q, Entry('A', 3))  # heappush is a method to add an
    heappush(q, Entry('B', 1))  # element
    heappush(q, Entry('C', 2))

    while q:
        next_item = heappop(q)  # heappop is a method to
        print(next_item)  # remove an element

    """

    """ Пирамидальная сортировка (реализация на списках)
    
    arr = [5, 3, 8, 12, 1, 0, 9]
    heap_sort(arr) # 12, 9, 8, 3, 1, 0, 5
    print(arr)
    
    """

    """ Максимальная куча из объектов класса Pair (реализация на модуле heapq) 
    
    # Достаточно просто переопределить метод __lt__ в хранимом кучей объекте.
    
    pq = [Pair(7, 0), Pair(3, 3), Pair(9, 4), Pair(4, 1), Pair(6, 2), Pair(1, 5)]
    heapify(pq)

    # работает до тех пор, пока максимальная куча не станет пустой
    while pq:
        # вывести следующий максимальный элемент из кучи
        print(heappop(pq))
        
    """

    """ Максимальная куча (реализация на модуле heapq).
    arr = [7, 4, 6, 3, 9, 1]
 
    # создает максимальную кучу из всех элементов в списке
    pq = MaxHeap(arr)
 
    # поп из максимальной кучи
    print(pq.pop())     # 9
    print(pq.pop())     # 7
    print(pq.pop())     # 6
 
    pq.push(10)
    pq.push(9)
 
    print(pq.pop())     # 10
    print(pq.pop())     # 9
    """


if __name__ == "__main__":
    execute_application()
