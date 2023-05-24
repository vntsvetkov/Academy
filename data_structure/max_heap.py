import heapq


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


class MaxHeap:

    # Инициализировать максимальную кучу
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    # Поместить элемент в максимальную кучу, сохраняя инвариантность кучи
    def push(self, item):
        heapq.heappush(self.data, -item)

    # Вытолкнуть самый большой элемент из максимальной кучи, сохраняя инвариантность кучи
    def pop(self):
        return -heapq.heappop(self.data)

    # Извлекать и возвращать текущее наибольшее значение, а также добавлять новый элемент
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)

    # Возвращает текущее наибольшее значение в максимальной куче
    def top(self):
        return -self.data[0]