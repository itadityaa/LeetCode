def twoSum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for i in range(len(nums)):
        if target - nums[i] in lookup:
            return [i, lookup[(target - nums[i])]]
        lookup[nums[i]] = i


print(twoSum(nums=[2, 7, 11, 15], target=9))
