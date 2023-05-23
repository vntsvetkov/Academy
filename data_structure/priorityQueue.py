class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __str__(self):
        return f"(Значение {self.item}; Приоритет {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.__queue])

    # for checking if the queue is empty
    def is_empty(self):
        return len(self.__queue) == 0

    # for inserting an element in the queue
    def insert(self, item, priority):
        self.__queue.append(Entry(item, priority))
        self.__queue.sort()

    # for popping an element based on max priority
    def delete(self):
        return self.__queue.pop().item


