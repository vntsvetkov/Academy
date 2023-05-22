class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass


class PriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.__queue])

    # for checking if the queue is empty
    def is_empty(self):
        pass

    # for inserting an element in the queue
    def insert(self, item, priority):
        pass

    # for popping an element based on max priority
    def delete(self):
        pass

