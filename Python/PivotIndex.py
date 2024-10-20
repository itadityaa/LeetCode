def pivotIndex(nums: list[int]) -> int:
    """My Solution"""
    if nums:
        for length in range(len(nums)):
            if sum(nums[:length]) == sum(nums[length + 1:]):
                return length
        return -1
    else:
        return -1


def BetterPivotIndex(nums: list[int]) -> int:
    """A Better Solution"""
    sumL = 0
    sumR = sum(nums)
    for i in range(len(nums)):
        sumR -= nums[i]
        if sumL == sumR:
            return i
        sumL += nums[i]
    return -1
