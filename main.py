from data_structure.queue import Queue
# from data_structure.deque import Deque
# from data_structure.linkedList import LinkedList

from collections import deque

def execute_application():
    '''
    linked_list = LinkedList()
    linked_list.add_first(1)
    linked_list.add_first(2)
    linked_list.add_last(3)
    linked_list.add_last(4)
    print(linked_list.remove_first()) # 2
    print(linked_list.remove_last()) # 4
    print(linked_list.remove_first()) # 1
    print(linked_list.remove_last()) # 3
    '''
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.peek())
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())


if __name__ == "__main__":
    execute_application()
