import random
import time


def selection_sort(arr: list, reverse: bool = False) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data
    for idx in range(n - 1):
        cur_limit = idx
        for cur in range(idx + 1, n):
            if reverse:
                if data[cur] > data[cur_limit]:
                    cur_limit = cur
            else:
                if data[cur] < data[cur_limit]:
                    cur_limit = cur

        if cur_limit != idx:
            data[idx], data[cur_limit] = data[cur_limit], data[idx]

    return data


if __name__ == '__main__':
    n = 1_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = selection_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')

        start = time.time()
        sorted_list = selection_sort(list_to_sort, reverse=True)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
