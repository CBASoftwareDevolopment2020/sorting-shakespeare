import random
import re
import time
from collections import defaultdict
from datetime import datetime as dt
from statistics import mean

import pandas as pd
from matplotlib import pyplot as plt

import bubble_sort
import heap_sort
import insertion_sort
import merge_sort
import quick_sort
import selection_sort
import trie


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8-sig") as file:
        return file.read()


def sanitize_string(content: str) -> list:
    content = content.lower()
    return re.findall("[a-z']+", content)


def log_time(name: str, runtime: float, n: int):
    if runtime > 0:
        with open('sorting-runtimes.csv', 'a') as file:
            file.write(f'{name}, {runtime}, {n}, {dt.now()}\n')


def time_function(function: callable, arr: list, timeout: int = 60, **kwargs) -> float:
    alphabet = kwargs.get('alphabet', None)
    reverse = kwargs.get('reverse', False)

    try:
        start = time.time()
        if alphabet:
            function(arr, alphabet, reverse=reverse)
        else:
            function(arr, reverse=reverse)

        time_elapsed = time.time() - start
        return time_elapsed
    except Exception as e:
        print(e)


def get_values(_dict: dict) -> tuple:
    keys = []
    values = []
    for key, value in sorted(_dict.items(), key=lambda x: int(x[0])):
        keys.append(key)
        avg = mean(value)
        values.append(avg)
    return keys, values


def reverse(arr: list) -> list:
    data = arr[:]
    n = len(data)
    if n < 2:
        return data
    for i in range(n // 2):
        data[i], data[-1 - i] = data[-1 - i], data[i]
    return data


reached_data_limit = []
functions = []

if __name__ == '__main__':
    text = read_file('shakespeare-complete-works.txt')
    words = sanitize_string(text)
    alphabet = sorted((list(set(''.join(words)))))
    iterations = 10

    n = len(words)
    limits = []
    for i in range(30):
        limits.append(min(n, 2 ** i))
        limits.append(max(1, int(n * 1 / 2 ** i)))
    limits = sorted(list(set(limits)))

    for limit in limits:
        for i in range(iterations):
            arr = random.sample(words, k=limit)

            time_function(trie.dict_trie_sort, arr, alphabet=alphabet)
            time_function(quick_sort.quick_sort_3way, arr)
            time_function(trie.list_trie_sort, arr, alphabet=alphabet)
            time_function(merge_sort.merge_sort, arr)
            time_function(heap_sort.heap_sort, arr)
            time_function(quick_sort.quick_sort, arr)
            time_function(insertion_sort.insertion_sort, arr)
            time_function(selection_sort.selection_sort, arr)
            time_function(bubble_sort.bubble_sort, arr)

            time_function(trie.dict_trie_sort, arr, alphabet=alphabet, reverse=True)
            time_function(quick_sort.quick_sort_3way, arr, reverse=True)
            time_function(trie.list_trie_sort, arr, alphabet=alphabet, reverse=True)
            time_function(merge_sort.merge_sort, arr, reverse=True)
            time_function(heap_sort.heap_sort, arr, reverse=True)
            time_function(quick_sort.quick_sort, arr, reverse=True)
            time_function(insertion_sort.insertion_sort, arr, reverse=True)
            time_function(selection_sort.selection_sort, arr, reverse=True)
            time_function(bubble_sort.bubble_sort, arr, reverse=True)

    df = pd.read_csv('sorting-runtimes.csv')

    times_dict = {func: defaultdict(list) for func in functions}

    for idx, row in df.iterrows():
        times_dict[row['Algorithm']][row['Data size']].append(row['Runtime'])

    xys_dict = {func: get_values(times_dict[func]) for func in functions}

    algs = []
    algs_reverse = []

    for alg, xys in xys_dict.items():
        if 'reversed_' in alg:
            algs_reverse.append(alg)
            plt.figure('algs_reverse')
        else:
            algs.append(alg)
            plt.figure('algs')

        plt.plot(xys[0], xys[1])

        plt.xlabel('Data size')
        plt.ylabel('Time (sec)')
        plt.xscale('log')
        plt.yscale('log')

        if 'reversed_' in alg:
            plt.legend(algs_reverse)
            plt.title(f'algs_reverse runtime {dt.now()}')
        else:
            plt.legend(algs)
            plt.title(f'algs runtime {dt.now()}')

    plt.show()
