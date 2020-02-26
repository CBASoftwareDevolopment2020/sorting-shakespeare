import random
import re
import time


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8-sig") as file:
        return file.read()


def sanitize_string(content: str) -> list:
    content = content.lower()
    return re.findall("[a-z']+", content)


def time_function(function: callable, **kwargs) -> float:
    arr = kwargs.get('arr', None)
    alphabet = kwargs.get('alphabet', None)
    start = time.time()
    if alphabet:
        function(arr, alphabet)
    else:
        function(arr)
    return time.time() - start


if __name__ == '__main__':
    import BubbleSort, HeapSort, InsertionSort, MergeSort, QuickSort, SelectionSort, Trie

    text = read_file('shakespeare-complete-works.txt')
    words = sanitize_string(text)
    alphabet = sorted((list(set(''.join(words)))))
    n = len(words)

    dict_trie_time = time_function(Trie.dict_trie_sort, arr=random.sample(words, k=n), alphabet=alphabet)
    list_trie_time = time_function(Trie.list_trie_sort, arr=random.sample(words, k=n), alphabet=alphabet)
    merge_time = time_function(MergeSort.merge_sort, arr=random.sample(words, k=n))
    heap_time = time_function(HeapSort.heap_sort, arr=random.sample(words, k=n))
    # quick_time = time_function(QuickSort.quick_sort, arr=random.sample(words, k=n))
    # selection_time = time_function(SelectionSort.selection_sort, arr=random.sample(words, k=n))
    # insertion_time = time_function(InsertionSort.insertion_sort, arr=random.sample(words, k=n))
    # bubble_time = time_function(BubbleSort.bubble_sort, arr=random.sample(words, k=n))

    print(f'Dict trie sort on {n} items took {dict_trie_time} seconds')
    print(f'List trie sort on {n} items took {list_trie_time} seconds')
    print(f'Merge sort on {n} items took {merge_time} seconds')
    print(f'Heap sort on {n} items took {heap_time} seconds')
    # print(f'Quick sort on {n} items took {quick_time} seconds')
    # print(f'Selection sort on {n} items took {selection_time} seconds')
    # print(f'Insertion sort on {n} items took {insertion_time} seconds')
    # print(f'Bubble sort on {n} items took {bubble_time} seconds')
