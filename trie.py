import random
import time

import MiniProject1


class ListNode(object):
    def __init__(self, alphabet: list):
        self.children = [None for _ in range(len(alphabet))]
        self.values = []


class ListTrie:
    def __init__(self, alphabet: list):
        self.root = ListNode(alphabet)
        self.alphabet = alphabet

    def index_of(self, char: str) -> int:
        idx = ord(char) - chr('a') + 1
        if idx < 0:
            idx = 0
        return idx

    def insert(self, key: str, value: object):
        node = self.root
        for char in key:
            if type(node.children[self.index_of(char)]) is not ListNode:
                node.children[self.index_of(char)] = ListNode(self.alphabet)
            node = node.children[self.index_of(char)]
        node.values.append(value)

    def get_values(self, node: ListNode):
        values = node.values
        if len(node.children) == 0:
            return values
        for char in self.alphabet:
            child = node.children[self.index_of(char)]
            if child:
                values.extend(self.get_values(child))
        return values


class DictNote(object):
    def __init__(self):
        self.children = {}
        self.values = []


class DictTrie:
    def __init__(self, alphabet: list):
        self.root = DictNote()
        self.alphabet = alphabet

    def insert(self, key: str, value: object):
        node = self.root
        for char in key:
            if char not in node.children.keys():
                node.children[char] = DictNote()
            node = node.children[char]
        node.values.append(value)

    def get_values(self, node: DictNote) -> list:
        values = node.values
        if len(node.children) == 0:
            return values
        for char in self.alphabet:
            child = node.children.get(char, None)
            if child:
                values.extend(self.get_values(child))
        return values


def list_trie_sort(arr: list, alphabet: list, reverse: bool = False) -> list:
    data = arr[:]
    if reverse:
        alphabet = MiniProject1.reverse(alphabet)
    trie = ListTrie(alphabet)
    for item in data:
        trie.insert(item, item)
    return trie.get_values(trie.root)


def dict_trie_sort(arr: list, alphabet: list, reverse: bool = False) -> list:
    data = arr[:]
    if reverse:
        alphabet = MiniProject1.reverse(alphabet)
    trie = DictTrie(alphabet)
    for item in data:
        trie.insert(item, item)
    return trie.get_values(trie.root)


if __name__ == '__main__':
    alphabet = [str(x) for x in range(10)]
    n = 1_000_000
    list_to_sort = random.choices(alphabet, k=n)
    start = time.time()
    sorted_list = list_trie_sort(list_to_sort, alphabet)
    time_elapsed = time.time() - start
    print(f'List Trie sort with {n} items took {time_elapsed} seconds')

    start = time.time()
    sorted_list = dict_trie_sort(list_to_sort, alphabet)
    time_elapsed = time.time() - start
    print(f'Dict Trie sort with {n} items took {time_elapsed} seconds')

    # start = time.time()
    # sorted_list = list_trie_sort(list_to_sort, alphabet, reverse=True)
    # time_elapsed = time.time() - start
    # print(f'List Trie sort with {n} items took {time_elapsed} seconds')

    # start = time.time()
    # sorted_list = dict_trie_sort(list_to_sort, alphabet, reverse=True)
    # time_elapsed = time.time() - start
    # print(f'Dict Trie sort with {n} items took {time_elapsed} seconds')
