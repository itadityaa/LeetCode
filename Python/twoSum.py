from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

  Args:
      nums (List[int]): List of integers
      target (int): Target sum

  Returns:
      List[int]: List of indices of the two numbers
  """  
  hash_map = {}
  for index, val in enumerate(nums):
      diff = target - val
      if diff in hash_map:
          return [hash_map[diff], index]
      hash_map[val] = index

nums = [2, 7, 2, 15]
print(twoSum(nums, 9)) # Output: [0, 1]