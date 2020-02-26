import random
import time


def selection_sort(arr: list) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data
    for idx in range(n - 1):
        cur_min = idx
        for cur in range(idx + 1, n):
            if data[cur] < data[cur_min]:
                cur_min = cur

        if cur_min != idx:
            data[idx], data[cur_min] = data[cur_min], data[idx]

    return data


if __name__ == '__main__':
    n = 1_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = selection_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
