import random
import time


def bubble_sort(arr: list, reverse: bool = False) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data

    for i in range(n):
        for j in range(n - i - 1):
            if reverse:
                if data[j] <= data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    return data


if __name__ == '__main__':
    n = 1_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = bubble_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')

        start = time.time()
        sorted_list = bubble_sort(list_to_sort, reverse=True)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
