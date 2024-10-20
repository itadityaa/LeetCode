def longestCommonPrefix(strs: list[str]) -> str:
    output = ""
    for characters in zip(*strs):
        # print(characters)
        if len(set(characters)) > 1:
            return output
        else:
            output += characters[0]
    return min(strs)


print(longestCommonPrefix(["flower", "flow", "flight"]))
