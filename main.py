from data_structure.priorityQueue import PriorityQueue
from data_structure.heapSort import heap_sort


def execute_application():
    import multiprocessing
    print(multiprocessing.cpu_count())
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
