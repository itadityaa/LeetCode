def climbStairs(n: int) -> int:
    '''This is Fibonacci Series'''
    # 0 step - 0 way, 1 step - 1 way, 2 step - 2 ways
    # 3 step - 3 ways, #4 steps - 5 ways, #5 steps - 8 ways and so on

    step_1 = 1
    step_2 = 1
    for steps in range(n):
        step_1, step_2 = step_1 + step_2, step_1
    return step_2


print(climbStairs(20))