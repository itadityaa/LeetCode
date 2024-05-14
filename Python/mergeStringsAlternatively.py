class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(max(len(word1), len(word2))):
            try:
                res.append(word1[i])
            except:
                pass
            try:
                res.append(word2[i])
            except:
                pass
        return(''.join(res))

# Test cases
test = Solution()
print(test.mergeAlternately("abc", "pqr") == "apbqcr")
print(test.mergeAlternately("ab", "pqrs") == "apbqrs")
print(test.mergeAlternately("a", "pqr") == "apqr")
print(test.mergeAlternately("abc", "p") == "apbc")
print(test.mergeAlternately("abc", "") == "abc")