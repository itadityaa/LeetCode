def summ(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + summ(arr[1:])


print(summ([1, 2, 3, 4, 5, 6]))
