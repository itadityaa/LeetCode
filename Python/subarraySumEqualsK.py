from typing import List

def subarraySum(nums: List[int], k: int) -> int:
  """Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

  Args:
      nums (List[int]): List of integers
      k (int): Target sum

  Returns:
      int: Total number of continuous subarrays whose sum equals to k
  """    
  count = 0
  prefix_sum = 0 
  hashmap = {0: 1}
  for ele in nums:
      prefix_sum += ele           
      if prefix_sum - k in hashmap:
          count += hashmap[prefix_sum - k]
      if prefix_sum not in hashmap:
          hashmap[prefix_sum] = 1
      else:
          hashmap[prefix_sum] += 1
  return count

nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k)) # Output: 2