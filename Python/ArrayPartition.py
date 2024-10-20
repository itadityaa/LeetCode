def arrayPairSum(nums: list[int]) -> int:
    nums.sort(reverse=True)
    total = 0
    for i in range(1, len(nums), 2):
        total += nums[i]
    return total


print(arrayPairSum([1, 4, 3, 2]))
