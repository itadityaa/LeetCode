import random


def quisearch(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quisearch(less) + [pivot] + quisearch(greater)


arr = [10, 2, 43, 53, 34, 12, 23]
print(quisearch(arr))