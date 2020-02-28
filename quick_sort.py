import random
import time


def quick_sort(arr: list, reverse: bool = False) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data

    idx = random.randint(0, n - 1)
    pivot = data[idx]
    data[0], data[idx] = data[idx], data[0]
    lower = []
    greater = []

    for x in data[1:]:
        if x <= pivot:
            lower.append(x)
        else:
            greater.append(x)

    if reverse:
        return quick_sort(greater, reverse=reverse) + [pivot] + quick_sort(lower, reverse=reverse)
    else:
        return quick_sort(lower) + [pivot] + quick_sort(greater)


def quick_sort_3way(arr: list, reverse: bool = False) -> list:
    data = arr[:]
    if len(data) < 2:
        return data

    pivot = random.choice(data)
    lower = []
    equal = []
    greater = []

    for x in data:
        if x < pivot:
            lower.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)

    if reverse:
        return quick_sort_3way(greater, reverse=reverse) + equal + quick_sort_3way(lower, reverse=reverse)
    else:
        return quick_sort_3way(lower) + equal + quick_sort_3way(greater)


if __name__ == '__main__':
    n = 1_000
    list_to_sort = random.choices(range(10 ** 3), k=n)
    try:
        start = time.time()
        sorted_list = quick_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Quick sort with {n} items took {time_elapsed} seconds')

        start = time.time()
        sorted_list = quick_sort_3way(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Quick sort 3way with {n} items took {time_elapsed} seconds')

        start = time.time()
        sorted_list = quick_sort(list_to_sort, reverse=True)
        time_elapsed = time.time() - start
        print(f'Quick sort with {n} items took {time_elapsed} seconds')

        start = time.time()
        sorted_list = quick_sort_3way(list_to_sort, reverse=True)
        time_elapsed = time.time() - start
        print(f'Quick sort 3way with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
