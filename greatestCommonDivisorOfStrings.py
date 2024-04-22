def gcdOfStrings(str1: str, str2: str) -> str:
  """Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

  Args:
      str1 (str): String 1
      str2 (str): String 2

  Returns:
      str: The largest string x such that x divides both str1 and str2.
  """    
  if str1 + str2 != str2 + str1:
      return ""
  if len(str1) == len(str2):
      return str1
  if len(str1) < len(str2):
      return gcdOfStrings(str1, str2[len(str1):])
  return gcdOfStrings(str1[len(str2):], str2)

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2)) # ABC