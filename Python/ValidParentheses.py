def isValid(s: str) -> bool:
    hash_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for bracket in s:
        if bracket not in hash_map:
            stack.append(bracket)
        else:
            if len(stack) > 0:
                last_element = stack.pop()
                if last_element != hash_map[bracket]:
                    return False
            else:
                return False
    return not stack


print(isValid('{}{[[])}'))
