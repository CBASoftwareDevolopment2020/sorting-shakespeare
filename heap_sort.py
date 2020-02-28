import random
import time


def max_heapify(data: list, n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        max_heapify(data, n, largest)


def min_heapify(data: list, n: int, i: int):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] <= data[smallest]:
        smallest = left
    if right < n and data[right] <= data[smallest]:
        smallest = right

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        min_heapify(data, n, smallest)


def heap_sort(arr: list, reverse: bool = False) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data

    for i in range(n, -1, -1):
        if reverse:
            min_heapify(data, n, i)
        else:
            max_heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        if reverse:
            min_heapify(data, i, 0)
        else:
            max_heapify(data, i, 0)

    return data


if __name__ == '__main__':
    n = 1_000_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = heap_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')

        start = time.time()
        sorted_list = heap_sort(list_to_sort, reverse=True)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
