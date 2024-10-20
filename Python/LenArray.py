# Length of Array using Recursion
def lenrecursive(arr):
    if not arr:
        return 0
    else:
        return 1 + lenrecursive(arr[1:])


print(lenrecursive([0, 1, 2, 3, 3, 2, 1, 0]))
