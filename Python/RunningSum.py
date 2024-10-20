def runningSum(nums: list[int]) -> list[int]:
    final_sum = []

    for num in range(len(nums)):
        if num == 0:
            final_sum.append(nums[num])
        else:
            final_sum.append((final_sum[num - 1] + nums[num]))
    return final_sum


print(runningSum([1, 1, 1, 1, 2]))
