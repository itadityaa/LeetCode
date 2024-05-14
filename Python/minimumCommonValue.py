from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
      """Find the minimum common value between two sorted arrays

      Args:
          nums1 (List[int]): A sorted list of integers
          nums2 (List[int]): A sorted list of integers

      Returns:
          int: The minimum common value between the two lists
      """        
      pointer1 = pointer2 = 0
      while pointer1 < len(nums1) and pointer2 < len(nums2):
          if nums1[pointer1] == nums2[pointer2]:
              return nums1[pointer1]
          elif nums1[pointer1] < nums2[pointer2]:
              pointer1 += 1
          else: pointer2 += 1
      return -1

# Test cases
sol = Solution()
print(sol.getCommon([1,2,3,4,5], [2,3,4,5,6])) # 2
print(sol.getCommon([1,2,3,4,5], [6,7,8,9,10])) # -1
print(sol.getCommon([1,2,3,4,5], [1,2,3,4,5])) # 1