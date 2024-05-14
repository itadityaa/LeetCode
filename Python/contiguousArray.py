from collections import defaultdict
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_count = res = 0
        sum_indices = defaultdict(int)
        
        for ind, num in enumerate(nums):
            sum_count += 1 if num == 1 else -1
            
            if sum_count == 0:
                res = ind + 1
            elif sum_count in sum_indices:
                res = max(res, ind - sum_indices[sum_count])
            else:
                sum_indices[sum_count] = ind
        
        return res
    
# Test cases
test = Solution()
print(test.findMaxLength([0,1]) == 2)
print(test.findMaxLength([0,1,0]) == 2)
print(test.findMaxLength([0,1,0,1]) == 4)