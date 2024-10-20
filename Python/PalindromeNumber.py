def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        x = str(x)
        print(x[::-1])
        return x == x[::-1]


print(isPalindrome(12121))
