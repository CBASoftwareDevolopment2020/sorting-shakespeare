import random
import time


def insertion_sort(arr: list, reverse: bool = False) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data

    for i in range(1, n):
        tmp = data[i]
        j = i - 1
        if reverse:
            while j >= 0 and data[j] <= tmp:
                data[j + 1] = data[j]
                j -= 1
        else:
            while j >= 0 and data[j] > tmp:
                data[j + 1] = data[j]
                j -= 1
        data[j + 1] = tmp

    return data


if __name__ == '__main__':
    n = 1_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = insertion_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')

        start = time.time()
        sorted_list = insertion_sort(list_to_sort, reverse=True)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
