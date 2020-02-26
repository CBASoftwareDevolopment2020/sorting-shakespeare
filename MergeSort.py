import random
import time


def merge(left, right):
    data = []
    left_idx = right_idx = data_idx = 0
    left_len, right_len = len(left), len(right)

    while left_idx < left_len and right_idx < right_len:
        if left[left_idx] < right[right_idx]:
            data.append(left[left_idx])
            left_idx += 1
        else:
            data.append(right[right_idx])
            right_idx += 1
        data_idx += 1

    while left_idx < left_len:
        data.append(left[left_idx])
        left_idx += 1
        data_idx += 1
    while right_idx < right_len:
        data.append(right[right_idx])
        right_idx += 1
        data_idx += 1

    return data


def merge_sort(arr: list) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    data = merge(left, right)
    return data


if __name__ == '__main__':
    n = 1_000_000
    list_to_sort = random.sample(range(10 ** 6), k=n)
    try:
        start = time.time()
        sorted_list = merge_sort(list_to_sort)
        time_elapsed = time.time() - start
        print(f'Merge sort with {n} items took {time_elapsed} seconds')
    except Exception as e:
        print(e)
