def tribonacci(n: int) -> int:

    trib_array = []

    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        for num in range(n + 1):
            if num < 2:
                trib_array.append(num)
            elif num == 2:
                trib_array.append(1)
            else:
                trib_array.append(trib_array[-1] + trib_array[-3] + trib_array[-2])
        return trib_array[-1]


print(tribonacci(50))
