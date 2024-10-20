def isSubsequence(s: str, t: str) -> bool:
    s_len, t_len = len(s), len(t)
    if s_len > t_len:
        return False
    elif s_len == 0:
        return True
    else:
        s_iterator, t_iterator = 0, 0
        while s_iterator < s_len and t_iterator < t_len:
            if s[s_iterator] == t[t_iterator]:
                s_iterator += 1
            t_iterator += 1
        return s_len == s_iterator


print(isSubsequence("abc", "abvc"))
