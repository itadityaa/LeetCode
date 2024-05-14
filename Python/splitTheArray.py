from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
      """You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:

      nums1.length == nums2.length == nums.length / 2.
      nums1 should contain distinct elements.
      nums2 should also contain distinct elements.
      Return true if it is possible to split the array, and false otherwise.

      Args:
          nums (List[int]): A list of integers

      Returns:
          bool: True if it is possible to split the array, and false otherwise
      """        
      hashMap = {}
      for num in nums:
          if num not in hashMap:
              hashMap[num] = 1
          else:
              hashMap[num] += 1
              if hashMap[num] > 2:
                  return False
      return True

# Test cases
sol = Solution()
print(sol.isPossibleToSplit([1,2,3,4])) # True
print(sol.isPossibleToSplit([1,2,3,4,5,6])) # True
print(sol.isPossibleToSplit([1,1,1,4,5,6,7,8])) # False
