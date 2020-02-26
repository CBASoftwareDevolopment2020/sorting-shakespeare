import random
import time


def quick_sort(arr: list) -> list:
    data = arr[:]
    if len(data) < 2:
        return data

    pivot = random.choice(data)
    data[0], data[data.index(pivot)] = data[data.index(pivot)], data[0]
    lower = [x for x in data[1:] if x <= pivot]
    upper = [x for x in data[1:] if x > pivot]
    return quick_sort(lower) + [pivot] + quick_sort(upper)


if __name__ == '__main__':
    n = 1_000_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = quick_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Quick sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
