import string
import re
import datetime


class TimeoutException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Reader:
    def __init__(self, path):
        self.content = ""
        self.words = []
        with open(path, "r", encoding="utf-8-sig") as file:
            self.content = file.read()
        self.sanitize()

    def sanitize(self):
        text = self.content.lower()
        self.words = re.findall("[a-z']+-?[a-z]*", text)
        # print("All words are lower case")
        # text = text.translate(str.maketrans("", "", string.punctuation))
        # print("Removed punctuation")
        # # self.words = text.split()
        # print("Content sanitized")


class Sorter:
    def __init__(self):
        self.timeout_sec = datetime.timedelta(minutes=5)

    def bubble(self, data: list) -> list:
        time_start = datetime.datetime.now()
        n = len(data)
        for i in range(n):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                time_elapsed = datetime.datetime.now() - time_start
                if time_elapsed > self.timeout_sec:
                    raise TimeoutException()
        return data

    def bucket(self, data: list) -> list:
        pass

    def counting(self, data: list) -> list:
        pass

    def heap(self, data: list) -> list:
        def heapify(data, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and data[left] > data[largest]:
                largest = left
            if right < n and data[right] > data[largest]:
                largest = right

            if largest != i:
                data[i], data[largest] = data[largest], data[i]
                heapify(data, n, largest)

        n = len(data)
        for i in range(n, -1, -1):
            heapify(data, n, i)
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0)
        return data

    def insertion(self, data: list) -> list:
        time_start = datetime.datetime.now()
        i = 1
        while i < len(data):
            tmp = data[i]
            j = i - 1
            while j >= 0 and data[j] > tmp:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = tmp
            i += 1
            time_elapsed = datetime.datetime.now() - time_start
            if time_elapsed > self.timeout_sec:
                raise TimeoutException()
        return data

    def merge(self, data: list) -> list:
        if len(data) > 1:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            self.merge(left)
            self.merge(right)

            l_idx = r_idx = data_idx = 0
            while l_idx < len(left) and r_idx < len(right):
                if left[l_idx] < right[r_idx]:
                    data[data_idx] = left[l_idx]
                    l_idx += 1
                else:
                    data[data_idx] = right[r_idx]
                    r_idx += 1
                data_idx += 1

            while l_idx < len(left):
                data[data_idx] = left[l_idx]
                l_idx += 1
                data_idx += 1
            while r_idx < len(right):
                data[data_idx] = right[r_idx]
                r_idx += 1
                data_idx += 1
        return data

    def quick(self, data: list) -> list:
        def partition(arr: list, low: int, high: int) -> int:
            pivot = arr[high]
            i = low
            for j in range(low, high + 1):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[high] = arr[high], arr[i]
            return i

        def quicksort(arr: list, low: int, high: int) -> list:
            if low < high:
                pi = partition(arr, low, high)
                quicksort(arr, low, pi - 1)
                quicksort(arr, pi + 1, high)
            return arr

        return quicksort(data, 0, len(data) - 1)

    def selection(self, data: list) -> list:
        time_start = datetime.datetime.now()
        for i in range(len(data) - 1):
            jmin = i
            for j in range(i + 1, len(data)):
                if data[j] < data[jmin]:
                    jmin = j
            if jmin != i:
                # tmp = data[i]
                # data[i] = data[jmin]
                # data[jmin] = tmp
                data[i], data[jmin] = data[jmin], data[i]
            time_elapsed = datetime.datetime.now() - time_start
            if time_elapsed > self.timeout_sec:
                raise TimeoutException()
        return data

    def trie(self, arr: list):
        pass
