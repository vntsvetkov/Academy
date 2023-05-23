from data_structure.priorityQueue import PriorityQueue
from data_structure.heapSort import heap_sort
from heapq import heapify, heappop, heappush
import time
from random import randint


def timer(f):
    def tmp(*args, **kwargs):
        begin = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print("Время выполнения функции: {}".format(end - begin))
        return res
    return tmp

@timer
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]

@timer
def my_sort(iterable: list):
    iterable.sort()


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


class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"{self.item}, {self.priority}"


def execute_application():
    '''
    arr = [5, 3, 8, 12, 1, 0, 9]
    heapify(arr)
    while arr:
        print(heappop(arr), end=" ")
    '''
    '''
    arr = [randint(1, 10) for _ in range(10000)]
    heapsort(arr)

    arr = [randint(1, 10) for _ in range(10000)]
    bubble_sorting(arr)
    '''

    q = []

    heappush(q, Entry('A', 3))  # heappush is a method to add an
    heappush(q, Entry('B', 1))  # element
    heappush(q, Entry('C', 2))

    while q:
        next_item = heappop(q)  # heappop is a method to
        print(next_item)  # remove an element

    '''
    arr = [5, 3, 8, 12, 1, 0, 9]
    heap_sort(arr) # 12, 9, 8, 3, 1, 0, 5
    print(arr)
    '''

    '''
    queue = PriorityQueue()
    queue.insert("Помыть машину", 10)
    queue.insert("Сходить в кино", 7)
    queue.insert("Сделать домашнюю работу", 15)
    queue.insert("Погладить кота", 1)
    while not(queue.is_empty()):
        print(queue.delete())
    '''

if __name__ == "__main__":
    execute_application()
