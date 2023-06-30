from collections.abc import Iterator, Iterable


class OurIterator(Iterator):
    __position: int = None
    __reverse: bool = False

    def __init__(self, collection, reverse=False):
        self.__collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self.__collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class ItemCollection(Iterable):
    def __init__(self, collection):
        self.__collection = collection

    def __iter__(self):
        return OurIterator(self.__collection)

    def get_reverse_iterator(self):
        return OurIterator(self.__collection, True)


'''
Источник: https://proglib.io/p/py-patterns
class OddNumbers(object):
    "An iterable object."

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        return OddIterator(self)

class OddIterator(object):
    "An iterator."

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self

numbers = OddNumbers(7)

for n in numbers:
    print(n)

'''



if __name__ == "__main__":
    collection = iter(ItemCollection(["Third", "First", "Second"]))

    print(next(collection))
    print(next(collection))
    print(next(collection))