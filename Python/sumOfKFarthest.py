'''You are given an array of length “len”, another item called k and an integer value x. Your job is to find the sum of k farthest items in the array from x.

First line has len, k and x respectively
2nd line has the array

Example :

Input :
5 3 20
21 4 15 17 11

Output :
30

4, 15 and 11 are farthest from 20. Thus, their sum will be the answer.'''

def sumOfKFarthest(len: int, k: int, x: int, arr: list):
  arr.sort(key = lambda y: abs(y - x))
  return sum(arr[-k:])

  # hashmap = {}
  # for num in arr:
  #   hashmap[num] = abs(num - x)
  # result = 0
  # for key, value in sorted(hashmap.items(), key = lambda x: x[1], reverse = True)[:k]:
  #   result += key
  # return result // This does not work because the hashmap does not store the count of the number of times a number appears in the array

len, k, x = map(int, input().split())

arr = list(map(int, input().split()))

print(sumOfKFarthest(len, k, x, arr)) # 30
