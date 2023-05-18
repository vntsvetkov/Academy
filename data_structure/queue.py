from data_structure.linkedList import LinkedList


class Queue:
    def __init__(self):
        self.__data = LinkedList()

    # enqueue(item) – добавление нового элемента в очередь.
    def enqueue(self, item):
        self.__data.add_last(item)

    # dequeue() – удаление и возврат очередного элемента в порядке «первым вошел, первым вышел» (FIFO).
    def dequeue(self):
        return self.__data.remove_first()

    # peek() – возврат(без удаления) очередного элемента в очереди в порядке FIFO.
    def peek(self):
        item = self.__data.remove_first()
        self.__data.add_first(item)
        return item

    # size() – возврат количества элементов в очереди (будет использоваться __len()__)
    def __len__(self):
        return len(self.__data)

    # is_empty() – возврат True, если в очереди нет элементов, иначе возврат False.
    def is_empty(self):
        return len(self.__data) == 0
