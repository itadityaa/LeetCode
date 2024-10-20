"""My Approach (Wrong)"""


def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1

            if t[i] in dict2:
                dict2[t[i]] += 1
            else:
                dict2[t[i]] = 1

        dict1_l = []
        dict2_l = []

        for key in dict1:
            dict1_l.append(dict1[key])
        for key in dict2:
            dict2_l.append(dict2[key])

        return dict1_l == dict2_l
    #Failed test case: "bbbaaaba" "aaabbbba"


"""Better Approach - Leetcode Solution"""


def BisIsomorphic(self, s: str, t: str) -> bool:
    mapping_s_t = {}
    mapping_t_s = {}

    for c1, c2 in zip(s, t):

        # Case 1: No mapping exists in either of the dictionaries
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1

        # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
        # it doesn't match in either of the dictionaries or both
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False

    return True