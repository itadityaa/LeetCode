class Solution:
    def alternateDigitSum(self, n: int) -> int:
      """Given an integer n, return the sum of its digits alternately

      Args:
          n (int): An integer

      Returns:
          int: The sum of the digits of n alternately
      """        
      # n_str = [x for x in str(n)]
      # n_str = [(-1)**x*int(n_str[x]) for x in range(len(n_str)) ]
      # return sum(n_str)

      res = 0
      sign = 1
      for digit in str(n):
          res += (sign*int(digit))
          sign *= -1
      return res

# Test cases
sol = Solution()
print(sol.alternateDigitSum(123)) # 2
print(sol.alternateDigitSum(12345)) # 3

