def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selsort(arr):
    sorted_array: list = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        sorted_array.append(arr.pop(smallest))
    return sorted_array


print(selsort([6, 2, 35, 6, 23, 5, 324, 6, 4, 6, 2, 2, 135, 6, 6, 4]))
