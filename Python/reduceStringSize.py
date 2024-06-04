''' You’re given a string where multiple characters are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below : 

Input :
aabbbbeeeeffggg

Output:
a2b4e4f2g3

Input :
abbccccc

Output:
ab2c5

'''

def reduceStringSize(s: str):
  if not s:
    return ''
  hashmap = {}
  for word in s:
    if word in hashmap:
      hashmap[word] += 1
    else:
      hashmap[word] = 1
  result = ''
  for key, value in hashmap.items():
    if value == 1:
      result += key
    else:
      result += key + str(value)

  return result

s = 'aabbbbeeeeffggg'
print(reduceStringSize(s)) # a2b4e4f2g3
s = 'abbccccc'
print(reduceStringSize(s)) # ab2c5