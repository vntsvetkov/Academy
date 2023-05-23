def heapify(lst, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and lst[left_child] > lst[largest]:
        largest = left_child

    if right_child < heap_size and lst[right_child] > lst[largest]:
        largest = right_child

    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]
        heapify(lst, heap_size, largest)


def heap_sort(lst):
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)



