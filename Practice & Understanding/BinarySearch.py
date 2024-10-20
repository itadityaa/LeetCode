def binsearch(arr, n):
    high = len(arr) - 1
    low = arr[0]
    count = 0
    while low <= high:
        count += 1
        mid = (high + low) // 2
        if n == arr[mid]:
            print(count)
            return mid
        elif n < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(count)
    return None


ans = binsearch([1, 9, 92, 3, 2, 31, 4], 32)
print(ans)
