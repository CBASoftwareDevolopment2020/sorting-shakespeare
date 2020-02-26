import random
import time


def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


def heap_sort(arr: list) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data

    for i in range(n, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

    return data


if __name__ == '__main__':
    n = 1_000_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = heap_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
